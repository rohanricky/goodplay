import json
import requests
import sys

URL = "http://localhost:5000"
#https://personalssistantv1.firebaseapp.com
'''
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js
'''
def send_message(text):
    url = URL + "/api"
    response = requests.post(url,headers={'Content-Type': 'application/json'},data=json.dumps({"data":text}))
    print(response.text)

if __name__=='__main__':
    data=sys.argv[1:]
    send_message(data)
