from os.path import join
import json
from NotionApi.Http import Httpapi
from NotionApi.NotionClass import NotionClass as NC
from NotionApi.Property import *
from NotionApi.Exception import InfoAndPass, TryToDo

class Page(NC, Httpapi):
    def __init__(self) -> None:
        super().__init__()
        self.object = "page"
        self.id = None
        self.parent = {}
        self.archived = False
        self.url = None
        self.created_time = None
        self.last_edited_time = None        
        self.icon = None
        self.cover = None
        self.properties = None

    def InitPage(self, Input:str or dict):
        if self.headers["Authorization"] == "":
            raise InfoAndPass("empty TOKEN.\nInitUser with TOKEN first.")
        json = Input if type(Input) == dict else self.RetrieveDatabase(self, Input).json()
        for name, value in json.items():
            a = getattr(self, name, None)
            if a == None:
                continue
            self.__dict__[name] = value

    @TryToDo
    def RetrievePage(self, Count_in=None, id_in=None):
        if self.headers["Authorization"] == "":
            raise InfoAndPass("empty TOKEN.\nInitUser with TOKEN first.")
        Count = self if Count_in == None else Count_in
        id = self.id if id_in == None else id_in
        result = Count.GET(join(Count.urlHead, "pages", id))
        if result.status_code != 200:
            info = json.dumps(result.json(), ensure_ascii=False, indent=4)
            raise InfoAndPass("Bad http return:\n" + info)
        return result

    @TryToDo
    def CreatePage(self):
        if self.headers["Authorization"] == "":
            raise InfoAndPass("empty TOKEN.\nInitUser with TOKEN first.")
        json1=dict(self)
        json2 = json1.copy()
        for key, val in json1.items():
            if val == None:
                del(json2[key])
        json1 = json2
        #print(json.dumps(json1, indent=4, ensure_ascii=False))
        result = self.POST(join(self.urlHead, "pages"), json=json1)
        print(json.dumps(result.json()))
        if result.status_code != 200:
            info = json.dumps(result.json(), ensure_ascii=False, indent=4)
            raise InfoAndPass("Bad http return:\n" + info)
        self.InitDatabase(result.json())
        return result

    @TryToDo
    def UpdatePage(self, Count_in=None, id_in=None):
        if self.headers["Authorization"] == "":
            raise InfoAndPass("empty TOKEN.\nInitUser with TOKEN first.")
        Count = self if Count_in == None else Count_in
        id = self.id if id_in == None else id_in
        result = self.PATCH(join(self.urlHead, "pages", id))
        if result.status_code != 200:
            info = json.dumps(result.json(), ensure_ascii=False, indent=4)
            raise InfoAndPass("Bad http return:\n" + info)
        return result

    def __getitem__(self, item):
        if item == "title":
            outputList = []
            for member in self.title:
                outputList.append(dict(member))
            return outputList
        else:
            return getattr(self, item, None)
        




