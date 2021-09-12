
from Conf import HKMLDatabase
import NotionAPI as napi


class Block(object):
    jsoninfo = None
    def __init__(self):
        pass

class HKMission(object):
    jsoninfo = {

    }
    databaseID = HKMLDatabase
    
    def __init__(self):
        self.MissionList = {}
        self.InitmissionList()


    def InitmissionList(self):
        jsoninfo = napi.QueryDatabase(HKMission.databaseID)
        jsoninfo = napi.AnaJson(jsoninfo)
        blockList = jsoninfo['results']

        
        for i in blockList:
            missionName = i['properties']['Mission']['title'][0]['plain_text']
            self.MissionList[missionName] = {
                'ID' : i['id'].replace('-', ''),
                'json' : {
                    'properties' : i['properties']
                }
            }
    

    def CheckMission(self):
        pass

    
    def UpdateMissionList(self):
        for mission, data in self.MissionList.items():
            data['json']['properties']['state']['checkbox'] = True
            data['json']['properties']['Log']['rich_text'] = [{
                'text' : {
                    'content' : "此日志由机器人生成。"
                }
            }]
            result = napi.UpdatePage(data['ID'], data['json'])
            print(napi.PrintJson(napi.AnaJson(result)))
        