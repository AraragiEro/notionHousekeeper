from typing import Text
import requests
import json

class Httpapi(object):
    def __init__(self):
        self.headers = {
            "Authorization" : "",
            "Notion-Version" : "2021-08-16"
        }
        self.urlHead = "https://api.notion.com/v1"

    def InitUser(self, TOKEN):
        self.headers["Authorization"] = TOKEN

    def GET(self, url):
        return requests.get(url, headers=self.headers)
        
    def POST(self, url, json=None, data=None):
        return requests.post(url, headers=self.headers, json=json, data=data)

    def PATCH(self, url, json):
        return requests.patch(url, headers=self.headers, json=json)

    def SpecialMemberList(self, childMemberList:dict):
        tmpMemberList = childMemberList.copy()
        memberList = vars(Httpapi())
        for member in memberList.keys():
            del(tmpMemberList[member])
        return tmpMemberList



def AnaJson(obj):
    return json.loads(obj.text)

def PrintJson(obj):
    return json.dumps(obj, ensure_ascii=False, indent=4)





