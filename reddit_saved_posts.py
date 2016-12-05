import praw
from pprint import pprint


def login():
    '''logs in the user using OAuth 2.0 and returns a redditor object for use'''
    user_agent = 'osx:reddit_saved_posts_search: v0.1 (by /u/idreamapple)'
    # app_scopes = 'account creddits edit flair history identity livemanage
    # modconfig modcontributors modflair modlog modothers modposts modself
    # modwiki mysubreddits privatemessages read report save submit subscribe
    # vote wikiedit wikiread'
    r = praw.Reddit('mysettings', user_agent=user_agent)
    return r


def show_saved_post_by_subreddit(saved_posts):
    local_subreddits = []
    for post in saved_posts:
        local_subreddits.append(post.subreddit.display_name)

    subreddits = {}
    print('Number of saved posts by subreddit -')
    for subreddit in local_subreddits:
        if subreddit not in subreddits:
            subreddits[subreddit] = 1
        else:
            subreddits[subreddit] += 1

    pprint(subreddits)


def main():
    reddit_obj = login()
    authenticated_user = reddit_obj.get_me()
    print('Welcome /u/{}. We have been expecting you.'.format(authenticated_user.name))
    saved = authenticated_user.get_saved(sort='new', time='all', limit=None)

    saved_posts = []
    saved_comments = []

    for post in saved:  # separate posts and comments
        if isinstance(post, praw.objects.Submission):
            saved_posts.append(post)
        elif isinstance(post, praw.objects.Comment):
            saved_comments.append(post)

    saved_posts_title = set()

    for post in saved_posts:    # create a set of saved posts titles
        saved_posts_title.add(post.title)

    # print('\n\n\n\nSaved comments - ')
    # for comment in saved_comments:
    #    pprint(comment.body)


if __name__ == '__main__':
    main()
