import NotionApi
from structure import DateAndTime as DandT


class Property(object):
    def __init__(self) -> None:
        self.type = None


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
class Text(Property):
    def __init__(self) -> None:
        self.name = None
        self.type = 'rich_text'
        self.rich_text = []

    # 根据notion返回初始化
    def __init__(self, json):
        # 最少需要多少信息?
        # 照搬
        try:
            self.rich_text = json[json.key[0]]['rich_text']
            return self.rich_text
        except:
            return None
        pass
        

    def Addtext(self, 
                text,
                bold = False,
                italic = False,
                strikethrough = False,
                underline = False,
                code = False,
                color = 'default'):

        self.rich_text.append(
        {
            "type" : self.type,
            "text" : {
                "content" : text
            },
            "annotations" : {
                "bold": bold,
                "italic": italic,
                "strikethrough": strikethrough,
                "underline": underline,
                "code": code,
                "color": color                
            }
        }
        )

class Checkbox(Property):
    def __init__(self) -> None:
        super().__init__()



"""
"日期时间段": {
    "id": "TobP",
    "type": "date",
    "date": {
        "start": "2021-09-13T00:00:00.000+08:00",
        "end": "2021-09-30T00:00:00.000+08:00"
    }
}
"""
class Data(Property):
    def __init__(self) -> None:
        self.type = "date"
        self.start = DandT()
        self.end = DandT()



class Title(Property):
    def __init__(self) -> None:
        super().__init__()