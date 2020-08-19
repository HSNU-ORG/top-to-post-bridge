import re


def update_post_format(post):
    """This function transform MySQL query into request-ready format.

    Args:
        post (tupple): 1 old format post

    Returns:
        A dictionary in ready to post format.
        ex: {
            title: ,
            genre: ,
            sub_genre_student: ,
            content: ,
            repeater_link: [{
                description: ,
                url:
            }]
        }
    """

    post_dict = {
        "title": post["title"]["rendered"],
        "content": post["content"]["rendered"],
        "last_name": post["acf"]["last_name"],
        "genre": post["acf"]["genre"],
        "repeater_link": post["acf"]["repeater_link"],
        "repeater_file": post["acf"]["repeater_file"],
    }

    if("sub_genre_race" in list(post["acf"].keys())):
        post_dict["sub_genre_race"] = post["acf"]["sub_genre_race"]

    if("sub_genre_student" in list(post["acf"].keys())):
        post_dict["sub_genre_student"] = post["acf"]["sub_genre_student"]

    print("Success on update_post_format")

    return post_dict
