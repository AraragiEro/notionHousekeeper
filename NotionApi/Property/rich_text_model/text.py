from NotionApi.NotionClass import NotionClass as NC

# 文本属性
class annotations(NC):
    def __init__(self):
        self.bold = False
        self.italic = False
        self.strikethrough = False
        self.underline = False
        self.code = False
        self.color = 'default'

    def LoadJson(self, json):
        try:
            self.bold = json["bold"]
            self.italic = json["italic"]
            self.strikethrough = json["strikethrough"]
            self.underline = json["underline"]
            self.code = json["code"]
            self.color = json["color"]
            return self
        except:
            return None

    
    def NewOne(self,
                bold = False,
                italic = False,
                strikethrough = False,
                underline = False,
                code = False,
                color = 'default'):
        self.bold = bold
        self.italic = italic
        self.strikethrough = strikethrough
        self.underline = underline
        self.code = code
        self.color = color
    


# 文本内容
class text(NC):
    def __init__(self):
        self.content = ""
        self.link = None

    def LoadJson(self, json):
        try:
            self.content = json["content"]
            self.link = json["link"]
            return self
        except:
            return None

    def NewOne(self, text, link=None):
        self.content = text
        self.link = link