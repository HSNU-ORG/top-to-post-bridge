from function.send import add_acf, add_post
from function.get import get_post
from function.transform import update_post_format


def main(request):

    # get posts
    post = get_post()

    # update post format
    post = update_post_format(post)

    # post it
    try:
        # add post
        id = add_post(post)

        # add acf
        add_acf(id, post)

        # print success message
        print(f"Success on {post}")
        return(f"Success on {post}")

    except ValueError:
        pass
