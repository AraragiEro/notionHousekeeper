from typing import Text
import requests
import json
from Conf import TOKEN, AUTHOR

class Httpapi(object):
    def __init__(self):
        self.headers = {
            "Authorization" : None,
            "Notion-Version" : "2021-08-16"
        }
        self.urlHead = "https://api.notion.com/v1"

    def InitUser(self, TOKEN):
        self.headers["Authorization"] = TOKEN

    def GET(self, url):
        return requests.get(url, headers=self.headers)
        
    def POST(self, url, json):
        return requests.post(url, headers=self.headers, json=json)

    def PATCH(self, url, json):
        return requests.patch(url, headers=self.headers, json=json)


def AnaJson(obj):
    return json.loads(obj.text)

def PrintJson(obj):
    return json.dumps(obj, ensure_ascii=False, indent=4)


def QueryDatabase(databaseID):
    jsoninfo = requests.request(
        "POST",
        "https://api.notion.com/v1/databases/{}/query".format(databaseID),
        headers = {
            AUTHOR : TOKEN,
            "Notion-Version" : "2021-08-16"
        }
    )
    return jsoninfo


def UpdatePage(pageID, data):
    jsoninfo = requests.request(
        "PATCH",
        "https://api.notion.com/v1/pages/{}".format(pageID),
        json=data,
        headers = {
            AUTHOR : TOKEN,
            "Notion-Version" : "2021-08-16",
        }
    )
    return jsoninfo


