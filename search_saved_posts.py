import praw
import prawcore
import webbrowser


def login():
    '''logs in the user using OAuth 2.0 and returns a redditor object for use'''
    username = input('Username: ')
    user_agent = 'reddit_saved_posts_search: v1.0 (for /u/{})'.format(
        username)
    r = praw.Reddit('mysettings', user_agent=user_agent)
    try:
        return r.user.me()
    except prawcore.exceptions.Forbidden:
        print('\nIt seems your credentials are invalid. Please check whether your praw.ini file is properly setup.')
        return None


def search(text, saved_posts):
    searched_posts = {}
    for index, post_id in enumerate(saved_posts):
        if text.lower() in saved_posts[post_id].lower():
            print('\n{}. {}'.format(index + 1, saved_posts[post_id]))
            searched_posts[index + 1] = post_id
    return searched_posts


def open_in_browser(url):
    webbrowser.open_new_tab(url)


def main():
    redditor = login()
    if redditor == None:
        print('\nStopping script...')
        return  # exit the script if unable to login

    print('Welcome /u/{}. I will help you search through your saved posts on reddit :)'.format(redditor))
    saved = redditor.saved(limit=None)

    saved_posts = []
    saved_comments = []
    saved_links = []

    for post in saved:  # separate out posts and comments
        if isinstance(post, praw.models.Submission):
            if 'reddit' in post.url:
                saved_posts.append(post)
            else:
                saved_links.append(post)
        elif isinstance(post, praw.models.Comment):
            saved_comments.append(post)

    saved_posts_title = {}
    saved_comments_body = {}
    saved_links_title = {}

    for post in saved_posts:    # create a list of saved posts' titles
        saved_posts_title[post.id] = post.title

    for comment in saved_comments:  # create a list of saved comment's body
        saved_comments_body[comment.id] = comment.body

    for post in saved_links:    # create a list of saved links' titles
        saved_links_title[post.id] = post.title

    while(True):
        choice = int(input(
            '\nSearch for [1] saved posts, [2] saved comments, [3] saved link posts [4] Exit: '))
        if choice == 4:  # exit the script
            print('Thank you for using this script. I hope to see you again soon :)')
            break

        text_to_search = input('\nEnter the text to search: ')

        if choice == 1:
            search_results = search(
                text=text_to_search, saved_posts=saved_posts_title)
        elif choice == 2:
            search_results = search(
                text=text_to_search, saved_posts=saved_comments_body)
        elif choice == 3:
            search_results = search(
                text=text_to_search, saved_posts=saved_links_title)
        else:
            print('\nPlease enter a valid choice.')
            continue

        post_number = int(input(
            '\nEnter the post number[0 to return to search] to open in your default browser: '))
        if post_number == 0:
            continue
        else:
            if choice == 1:
                for post in saved_posts:
                    try:
                        if post.id == search_results[post_number]:
                            open_in_browser(post.url)
                            break
                    except KeyError:
                        print('Please enter a valid post number.')
                        break
            elif choice == 2:
                for post in saved_comments:
                    try:
                        if post.id == search_results[post_number]:
                            open_in_browser(post.link_url + post.id)
                            break
                    except KeyError:
                        print('Please enter a valid post number.')
                        break
            elif choice == 3:
                for post in saved_links:
                    try:
                        if post.id == search_results[post_number]:
                            link_choice = int(
                                input('\n[1] to open link in browser, [2] to open reddit post in browser: '))
                            if link_choice == 1:
                                open_in_browser(post.url)
                                break
                            elif link_choice == 2:
                                open_in_browser(
                                    'https://www.reddit.com' + post.permalink)
                                break
                            else:
                                print('\nPlease enter a valid choice.')
                                break
                    except KeyError:
                        print('Please enter a valid post number.')
                        break


if __name__ == '__main__':
    main()
