#!/bin/python3

import requests
import json
import time

# personnal model
from Conf import TOKEN, AUTHOR
from NotionApi import NotionAPI as napi
import block



datal = requests.request(
    "GET",
    "https://api.notion.com/v1/databases/72128a62706c4af0884375aac96d7f31",
    headers = {
        "{}".format(AUTHOR) : "{}".format(TOKEN),
        "Notion-Version" : "2021-08-16"
    }
)

pager = requests.request(
    "GET",
    "https://api.notion.com/v1/pages/2544c49ae5ad41088deefa9b15f695f1",
    headers = {
        "{}".format(AUTHOR) : "{}".format(TOKEN),
        "Notion-Version" : "2021-08-16"
    }
)

dataq = requests.request(
    "POST",
    "https://api.notion.com/v1/databases/72128a62706c4af0884375aac96d7f31/query",
    headers = {
        "{}".format(AUTHOR) : "{}".format(TOKEN),
        "Notion-Version" : "2021-08-16"
    }
)


def main():
    #houseKeeper = block.HKMission()
    #houseKeeper.UpdateMissionList()

    class test():
        def __init__(self) -> None:
            self.a = 0
            self.b = 0

    a = test()
    vars(a)


if __name__ == '__main__':
    main()