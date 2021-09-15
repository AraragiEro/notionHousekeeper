from os.path import join
import json

from requests import NullHandler
import requests
from NotionApi.Http import Httpapi
from NotionApi.NotionClass import NotionClass as NC
from NotionApi.Property import *
from requests.models import Response
from NotionApi.Page import Page
from NotionApi.Exception import InfoAndPass, TryToDo

class Database(NC, Httpapi):
    def __init__(self, TOKEN:str = None) -> None:
        super().__init__()
        self.parent = {}
        self.object = "database"
        self.id = ""
        self.cover = None
        self.icon = None
        self.created_time = None
        self.last_edited_time = None
        self.title = []
        self.properties = {}
        if TOKEN != None:
            self.InitUser(TOKEN)
        
    def InitDatabase(self, Input:str or dict):
        if self.headers["Authorization"] == "":
            raise InfoAndPass("empty TOKEN.\nInitUser with TOKEN first.")
        json = Input if type(Input) == dict else self.RetrieveDatabase(self, Input).json()
        for name, value in json.items():
            a = getattr(self, name, None)
            if a == None:
                continue
            if name == "title":
                for text in value:
                    txtmem = rich_text.richTextText()
                    txtmem.LoadJson(text)
                    self.__dict__[name].append(txtmem)
            else:
                self.__dict__[name] = value

    @TryToDo
    def QueryDatabase(self, Count_in=None, id_in=None):
        Count = self if Count_in == None else Count_in
        id = self.id if id_in == None else id_in
        result = Count.POST(join(Count.urlHead, "databases", id, "query"))
        if result.status_code != 200:
            info = json.dumps(result.json(), ensure_ascii=False, indent=4)
            raise InfoAndPass("Bad http return:\n" + info)
        return result

    @TryToDo
    def CreateDatebase(self):
        json1=dict(self)
        json2 = json1.copy()
        for key, val in json1.items():
            if val == None:
                del(json2[key])
        json1 = json2
        #print(json.dumps(json1, indent=4, ensure_ascii=False))
        result = self.POST(join(self.urlHead, "databases"), json=json1)
        print(json.dumps(result.json()))
        if result.status_code != 200:
            info = json.dumps(result.json(), ensure_ascii=False, indent=4)
            raise InfoAndPass("Bad http return:\n" + info)
        self.InitDatabase(result.json())
        return result 

    @TryToDo
    def UpdateDatebase(self, Count_in=None, id_in=None):
        Count = self if Count_in == None else Count_in
        id = self.id if id_in == None else id_in
        result = self.PATCH(join(self.urlHead, "databases", id))
        if result.status_code != 200:
            info = json.dumps(result.json(), ensure_ascii=False, indent=4)
            raise InfoAndPass("Bad http return:\n" + info)
        return result 

    @TryToDo
    def RetrieveDatabase(self, Count_in=None, id_in=None):
        Count = self if Count_in == None else Count_in
        id = self.id if id_in == None else id_in
        result = Count.GET(join(Count.urlHead, "databases", id))
        if result.status_code != 200:
            info = json.dumps(result.json(), ensure_ascii=False, indent=4)
            raise InfoAndPass("Bad http return:\n" + info)
        return result

    @TryToDo
    def ListDatabase(self):
        pass

    def __getitem__(self, item):
        if item == "title":
            outputList = []
            for member in self.title:
                outputList.append(dict(member))
            return outputList
        else:
            return getattr(self, item, None)
    
    