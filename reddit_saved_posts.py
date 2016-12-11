import praw
from pprint import pprint
from getpass import getpass

def login():
    '''logs in the user using OAuth 2.0 and returns a redditor object for use'''
    username = input('Username: ')
    password = getpass(prompt='Password: ')
    user_agent = 'osx:reddit_saved_posts_search: v0.1 (by /u/{})'.format(username)
    r = praw.Reddit('mysettings', user_agent=user_agent, username=username, password=password)
    return r.user.me()


def show_saved_post_by_subreddit(saved_posts):
    subreddit_names = []
    for post in saved_posts:
        subreddit_names.append(post.subreddit.display_name)

    subreddits = {}
    print('Number of saved posts by subreddit -')
    for subreddit in subreddit_names:
        if subreddit not in subreddits:
            subreddits[subreddit] = 1
        else:
            subreddits[subreddit] += 1

    pprint(subreddits)


def search(text, saved_posts):
    i = 1
    for title in saved_posts:
        if text in title:
            print('\n{}. {}'.format(i, title))
            i += 1


def main():
    redditor = login()
    print('Welcome /u/{}. We have been expecting you.'.format(redditor))
    saved = redditor.saved(limit=None)

    saved_posts = []
    saved_comments = []

    for post in saved:  # separate out posts and comments
        if isinstance(post, praw.models.Submission):
            saved_posts.append(post)
        elif isinstance(post, praw.models.Comment):
            saved_comments.append(post)

    saved_posts_title = []

    for post in saved_posts:    # create a list of saved posts' titles
        saved_posts_title.append(post.title)
        # print(post.title)
    while(True):
        text_to_search = input('\nEnter the text to search:')
        search(text=text_to_search, saved_posts=saved_posts_title)
        url = print('\n[Post Number] to open the link in your default web browser')


if __name__ == '__main__':
    main()
