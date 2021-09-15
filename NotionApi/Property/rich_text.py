from NotionApi.NotionClass import NotionClass as NC
from NotionApi.Property.rich_text_model.text import text, annotations
"""
"rich_text": {
    "id": "%3BziQ",
    "type": "rich_text",
    "rich_text": [
        {
            "type": "text",
            "text": {
                "content": "此日志由机器人生成。",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "此日志由机器人生成。",
            "href": null
        }
    ]
}
"""

class richTextText(NC):
    def __init__(self) -> None:
        self.type = "text"
        self.text = text()
        self.annotations = annotations()

    def LoadJson(self, json:dict):
            self.type = json["type"]
            try:
                tmpText = text()
                tmpAnno = annotations()
                self.text = tmpText.LoadJson(json["text"])
                self.annotations = tmpAnno.LoadJson(json["annotations"])
            except:
                return None

    def NewOne(self, 
            str,
            link = None,
            bold = False,
            italic = False,
            strikethrough = False,
            underline = False,
            code = False,
            color = 'default'):
        self.text.NewOne(str, link)
        self.annotations.NewOne(bold, italic, strikethrough, underline, code, color)

    def __getitem__(self, item):
        if item == "text" or item == "annotations":
            item = getattr(self, item)
            item = dict(item)
            return item
        else:
            return super().__getitem__(item)


class rich_text(NC):
    def __init__(self):
        self.type = "rich_text"
        self.rich_text = []

    def LoadJson(self, json:dict):
        for memberJson in json["rich_text"]:
            tmpMember = richTextText()
            self.rich_text.append(tmpMember.NewOne(memberJson))

    def AddText(self, newText):
        self.rich_text.append(newText)

    def __getitem__(self, item):
        if item == "rich_text":
            outputList = []
            for member in self.rich_text:
                outputList.append(dict(member))
            return outputList
        else:
            return super().__getitem__(item)

    

