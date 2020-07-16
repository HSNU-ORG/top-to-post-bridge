import os
import requests


def get_post():
    """This function get 1 post from old database.

    Returns:
        A json.
    """
    r = requests.get(
        url='https://wordpress.hsnu.org/wp-json/wp/v2/top?per_page=1')

    print("Success on mysql.py")

    return r.json()[0]
