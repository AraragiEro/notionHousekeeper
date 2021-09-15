import json

class NotionClass(object):
    def __init__(self) -> None:
        super().__init__()

    def LoadJson(self, json:dict):
        pass


    def NewOne(self):
        pass

    def __str__(self) -> str:
        printStr = dict(self)
        printStr = json.dumps(printStr, indent=4, ensure_ascii=False)
        return printStr

    def keys(self):
        member = vars(self).keys()
        return [x for x in member]


    def __getitem__(self, item):
        return getattr(self, item)