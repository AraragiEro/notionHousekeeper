from NotionApi.Page import Page
from NotionApi.DataBase import Database
from NotionApi.Http import Httpapi
import json, requests
from NotionApi.Exception import TryToDo
import uuid

AUTHOR = "Authorization"
TOKEN = "secret_deky50Il8WOH0E3yJaX2db5abrWpBoXbIOlCZ8aKGTB"
pageid = "33d427ffbd764574a6d8f3879a9e2f09"
Databaseid = "47b60c2e58984585baa40586897f0182"



@TryToDo
def main():
    newDatebase = Database(TOKEN)
    newDatebase.InitDatabase(Databaseid)
    newDatebase.id = None
    newDatebase.created_time = None
    newDatebase.last_edited_time = None
    newDatebase.title[0].text.content = "管家面板-复制品"
    del(newDatebase.parent["type"])
    newDatebase.parent["page_id"] = "4351ca947aaf498694afdeed22339910"
    for value in newDatebase.properties.values():
        del(value["id"])
        #del(value["type"])
        #del(value["name"])
    newDatebase.CreateDatebase()
    print(newDatebase)
    #print(json.dumps(rd.json(), indent=4, ensure_ascii=False))
    #print(type(rd) == requests.models.Response)

# 测试page模块
"""
def main():
    zhucctCount = Httpapi()
    zhucctCount.InitUser(TOKEN)
    newPage = Page()
    r = newPage.RetrievePage(zhucctCount, pageid)
    print(newPage)
    #print(dict(newPage))
"""

"""
def main():
    #houseKeeper = block.HKMission()
    #houseKeeper.UpdateMissionList()

    a = rich_text.rich_text()q
    b = rich_text.richTextText()
    b.NewOne("hallo world")
    a.AddText(b)
    print(a)
"""


if __name__ == '__main__':
    main()