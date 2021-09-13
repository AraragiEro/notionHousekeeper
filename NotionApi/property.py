import NotionApi


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
        self.rich_text = [i for i in json.value]
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





class Checkbox(object):
    def __init__(self) -> None:
        super().__init__()


class Data(object):
    def __init__(self) -> None:
        super().__init__()


class Title(object):
    def __init__(self) -> None:
        super().__init__()