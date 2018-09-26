from config import keys
import requests
from datetime import datetime
import base64
import urllib.parse
import hashlib
import json

class Lbs():
    ak = keys.BAIDUMAPAK
    sk = keys.BAIDUMAPSK
    routerPlanningDrivingApi = 'http://api.map.baidu.com/direction/v2/driving?'

    def getBaiDuRouteMatrix(self):
        p = self.routerPlanningDrivingApi + self.getBaiDuRouteMatrixParams()
        r = requests.get(p, {})
        resultDic = json.loads(r.text)
        if resultDic['status'] == 0 and resultDic['result']['total'] > 0:
            return resultDic['result']['routes'][0]
        else:
            print('百度地图接口读取失败：' + resultDic['message'])
        return None
    def getBaiDuRouteMatrixParams(self):
        queryStr = 'ak='+self.ak+'&origin=39.956945,116.792789&' + \
                'destination=39.922411,116.666881&tactics=0&output=json'
        encodedStr = urllib.parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
        m2 = hashlib.md5()
        m2.update((encodedStr + self.sk).encode("utf-8"))
        sn = m2.hexdigest()
        # queryStr += '&sn=' + sn
        return queryStr