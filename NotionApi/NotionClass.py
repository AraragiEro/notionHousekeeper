from abc import abstractmethod


class NotionClass(object):
    def __init__(self) -> None:
        super().__init__()

    def LoadJson(self, json:dict):
        pass


    def NewOne(self):
        pass


    def keys(self):
        member = vars(self).keys()
        return [x for x in member]


    def __getitem__(self, item):
        return getattr(self, item)