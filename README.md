# Search for reddit saved posts
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/hyperium/hyper/master/LICENSE) [![Python version](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-350/)

Hello!
I created this script to help users search through their saved posts/comments on reddit.

## Setup
In the terminal run the following code - 
```shell
$ pip install -r requirements.txt
```

Before using the script you must create your own app to obtain a public and a secret key. This can be done [here](https://ssl.reddit.com/prefs/apps).

Once you obtain your keys, create a new file in any text editor with the following content -
> [mysettings]

> client_id = YOUR_PUBLIC_APP_ID

> client_secret = YOUR_SECRET_APP_ID

> password = YOUR_PASSWORD

> username = YOUR_USERNAME

Save it as `praw.ini` .
Place it in your local working directory.

## Running the script
The script is directly run from the terminal.
```shell
$ python search_saved_posts.py 
```

