from NotionApi.Property.rich_text import rich_text
from typing import Type
from NotionApi.NotionClass import NotionClass as NC
from NotionApi.Property import rich_text

def main():
    #houseKeeper = block.HKMission()
    #houseKeeper.UpdateMissionList()

    a = rich_text.rich_text()
    b = rich_text.richTextText()
    b.NewOne("hallo world")
    a.rich_text.append(b)
    print(dict(a))



if __name__ == '__main__':
    main()