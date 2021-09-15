from os.path import join
from NotionApi.Property import *
from NotionApi.Http import Httpapi
from NotionApi.NotionClass import NotionClass as NC
from NotionApi.Property import *

class Page(NC, Httpapi):
    def __init__(self) -> None:
        self.object = "page"
        self.id = None
        self.parent = {}
        self.archived = False
        self.url = None
        self.icon = None
        self.cover = None
        self.properties = None

    def RetrievePage(self, Httpapi, id):
        result = Httpapi.GET(join(Httpapi.urlHead, "pages", id))
        if result.status_code != 200:
            return result
        
        json = result.json()
        self.id = json["id"]
        self.parent = json["parent"]
        self.archived = json["archived"]
        self.url = json["url"]
        self.icon = json["icon"]
        self.cover = json["cover"]
        self.properties = json["properties"]
        return result

    def CreatPage(self):
        result = Httpapi.POST(join(Httpapi.urlHead, "pages", self.id),
                              json = dict(self))
        if result.status_code == 200:
            return result
        else:
            return None

    def UpdatePage(self):
        result = Httpapi.PATCH(join(Httpapi.urlHead, "pages", self.id),
                               json = dict(self))
        if result.status_code == 200:
            return result
        else:
            return Non
        




