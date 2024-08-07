'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = '2UqxS-yWZhF3oaV7Jl5iDUcN7v1BP1dp'


def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """ 
    post_params = {
        "api_dev_key": API_DEV_KEY,
        "api_option": "paste",
        "api_paste_code": body_text,
        "api_paste_name": title,
        "api_paste_expire_date": expiration,
        "api_paste_private": 0 if listed else 1
    } 

    print("Creating new paste...", end="")
    response = requests.post(PASTEBIN_API_POST_URL,data=post_params)

    if response.status_code == requests.codes.ok:
        print("Success!")
        return response.text
    else:
        print("Failure :(")
        print(f"{response.status_code} {response.reason} ({response.text})")
        return
    