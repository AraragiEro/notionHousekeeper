from os import X_OK
from os.path import join
import json
from NotionApi.Http import Httpapi
from NotionApi.NotionClass import NotionClass as NC
from NotionApi.Property import *
from NotionApi.Exception import InfoAndPass, TryToDo

__all__ = ["PragraphBlock"]

class Block(NC, Httpapi):
    def __init__(self, input = None):
        if type(self) == Block:
            raise InfoAndPass("don't use base block class to init\nuse block.InitBlock() instead")
        super().__init__()
        print(type(self))
        self.object = "block"
        self.id = None
        self.created_time = None
        self.last_edited_time = None
        self.has_children = None
        self.type = None

    def InitBlock(self, Input:str or dict):
        if self.headers["Authorization"] == "":
            raise InfoAndPass("empty TOKEN.\nInitUser with TOKEN first.")
        json = Input if type(Input) == dict else self.RetrieveDatabase(self, Input).json()
        outputBlockClass = eval(json["type"])
        output = outputBlockClass()
        for name, value in json.items():
            a = getattr(self, name, None)
            if a == None:
                continue
            output.__dict__[name] = value        

    def RetriveBlock(self, Input:str or dict):
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

    def UpdateBlock(self):
        pass

    def RetriveBlockChildren(self):
        pass

    def AppendBlockChildren(self):
        pass

    def DeleteBlock(self):
        pass

class PragraphBlock(Block):
    def __init__(self) -> None:
        super().__init__()
        print(type(self))
        self.paragraph = {}