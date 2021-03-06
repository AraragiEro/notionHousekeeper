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
        member = vars(self)
        SpecialMemberList = getattr(self, "SpecialMemberList", None)
        if SpecialMemberList != None:
            member = SpecialMemberList(member)
        return [x for x in member.keys()]


    def __getitem__(self, item):
        return getattr(self, item, None)