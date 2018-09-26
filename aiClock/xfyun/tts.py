from config import keys
import requests
import time
from datetime import datetime
import base64
import hashlib

class XFtts():
    APPID = keys.XFAPPID
    API_KEY = keys.XFAPIKEY
    ttsUrl = 'http://api.xfyun.cn/v1/service/v1/tts'
    aue = 'raw'
    def requestTTS(self, route):
        return requests.post(self.ttsUrl,headers=self.getTTSHeader(),
                    data=self.getTTSBody("线路距离:{0}公里,耗时:{1}分钟".format(round(route['distance'] / 1000),round(route['duration'] / 60))))
    def getTTSHeader(self):
        curTime = str(int(time.time()))
        param = "{\"aue\":\""+self.aue+"\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\"xiaoyan\",\"engine_type\":\"intp65\"}"
        paramBase64 = base64.b64encode(param.encode("utf-8"))
        m2 = hashlib.md5()
        m2.update((self.API_KEY + curTime).encode("utf-8") + paramBase64)
        checkSum = m2.hexdigest()
        header ={
            'X-CurTime':curTime,
            'X-Param':paramBase64,
            'X-Appid':self.APPID,
            'X-CheckSum':checkSum,
            'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
        }
        return header
    def getTTSBody(self, text):
        data = {'text':text}
        return data