import json
import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth


def add_acf(id, post):
    """
    This function send request to ACF REST API.

    Args:
        id (int):
            The targe post id.
            ex: 24

        obj (obj):
            The post obj directly from rest api.

    Returns:
        success: {"status": "success", "response": (dict), "id": (str)}
        error: {"status": "error", "response": (dict), "id": (str)}

    """
    # load .env
    load_dotenv()

    # data to post
    payload = {
        "fields": {
            "genre": post["acf"]["genre"],
            "sub_genre_student": post["acf"]["sub_genre_student"],
            "repeater_link": post["acf"]["repeater_link"],
            "repeater_file": post["acf"]["repeater_file"],
            "last_name": post["acf"]["last_name"]
        }
    }

    # send request to add metadata (ACF)
    r = requests.post('https://wordpress.hsnu.org/index.php/wp-json/acf/v3/spost/{id}'.format(id=id),
                      json=payload, auth=HTTPBasicAuth(os.getenv("WORDPRESS_ACCOUNT"), os.getenv("WORDPRESS_PASSWORD")))

    # if success
    if json.loads(r.content)["acf"]["genre"] == post["acf"]["genre"]:
        print("Success on add_acf()")
        return {"status": "success", "response": json.loads(r.content), "id": id}
    # if error
    else:
        print({"status": "error", "response": json.loads(r.content), "id": id})
        return {"status": "error", "response": json.loads(r.content), "id": id}


def add_post(post):
    """This function send request to WP REST API.


    Args:
        post (obj): object directly from rest api.

    Returns:
        success: id (int)

    Raises:
        ValueError: If Wordpress return error
    """

    # load .env
    load_dotenv()

    # data to post
    payload = {
        "title": post["title"]["rendered"],
        "content": post["content"]["rendered"],
        "status": "publish"
    }

    # send request to add post (without metadata)
    r = requests.post('https://wordpress.hsnu.org/wp-json/wp/v2/spost',
                      json=payload, auth=HTTPBasicAuth(os.getenv("WORDPRESS_ACCOUNT"), os.getenv("WORDPRESS_PASSWORD")))

    # if success
    if r.status_code == 201:
        print("Success on add_post()")
        return json.loads(r.content)["id"]

    # if error
    else:
        print(json.loads(r.content))
        raise ValueError(f"ADD_POST_ERROR: There is error for post {json.loads(r.content)} in add_post() process. \
                            Error message from wp: {json.loads(r.content)}")
