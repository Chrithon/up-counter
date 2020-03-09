import requests
import json

def get_username(UID,Cookie):
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    headers = {"User-Agent": user_agent,
    'Cookie':Cookie}
    req = requests.get ("https://api.bilibili.com/x/space/acc/info?mid=" + UID + "&jsonp=jsonp",headers=headers)
    text = req.text
    answer= json.loads(text)
    username = answer['data']['name']
    return username

def get_views(UID,Cookie):
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    headers = {"User-Agent": user_agent,
    'Cookie':Cookie}
    req = requests.get ("https://api.bilibili.com/x/space/upstat?mid=9834737&type=jsonp",headers=headers)
    text = req.text
    answer = json.loads(text)
    views = answer['data']['archive']['view']
    return views

def get_reads(UID,Cookie):
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    headers = {"User-Agent": user_agent,
    'Cookie':Cookie}
    req = requests.get ("https://api.bilibili.com/x/space/upstat?mid=9834737&type=jsonp",headers=headers)
    text = req.text
    answer = json.loads(text)
    reads = answer['data']['article']['view']
    return reads

def get_likes(UID,Cookie):
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    headers = {"User-Agent": user_agent,
    'Cookie':Cookie}
    req = requests.get ("https://api.bilibili.com/x/space/upstat?mid=9834737&type=jsonp",headers=headers)
    text = req.text
    answer = json.loads(text)
    likes = answer['data']['likes']
    return likes

def get_fans(Cookie):
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    headers = {"User-Agent": user_agent,
    'Cookie':Cookie}
    req = requests.get ("https://api.bilibili.com/x/web-interface/nav/stat",headers=headers)
    text = req.text
    fans = json.loads(text)
    followers = fans['data']['follower']
    return followers
    