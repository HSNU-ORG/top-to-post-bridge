from function.request import add_acf, add_post
from function.mysql import get_post
from function.transform import update_post_format


def main(request):

    # get posts
    post = get_post()

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


if __name__ == "__main__":
    main(1)
