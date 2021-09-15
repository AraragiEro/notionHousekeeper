from NotionApi.Page import Page
from NotionApi.Http import Httpapi

AUTHOR = "Authorization"
TOKEN = "secret_deky50Il8WOH0E3yJaX2db5abrWpBoXbIOlCZ8aKGTB"
pageid = "33d427ffbd764574a6d8f3879a9e2f09"
def main():
    zhucctCount = Httpapi()
    zhucctCount.InitUser(TOKEN)
    newPage = Page()
    r = newPage.RetrievePage(zhucctCount, pageid)
    print(newPage)
    #print(dict(newPage))

"""
def main():
    #houseKeeper = block.HKMission()
    #houseKeeper.UpdateMissionList()

    a = rich_text.rich_text()
    b = rich_text.richTextText()
    b.NewOne("hallo world")
    a.AddText(b)
    print(a)
"""


if __name__ == '__main__':
    main()