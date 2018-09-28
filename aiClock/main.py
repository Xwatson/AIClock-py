import threading
import time
from baiduMap import lbs
from xfyun import tts
from playAudio import play

class myTherad(threading.Thread):
    def run(self):
        # 获取路线
        route = self.getBaiduLbs()
        # 转换语音
        ttsr = self.getXFTTS(route)
        # 播放语音
        self.playAudio(ttsr)
        """ while True:
            time.sleep(1)
            self.getBaiDuRouteMatrix() """
    def getBaiduLbs(self):
         # 获取百度驾车路线
        baiduLbs = lbs.Lbs()
        return baiduLbs.getBaiDuRouteMatrix()
    def getXFTTS(self, route):
        # 讯飞语音合成
        if not route is None:
            # 讯飞语音api
            xftts = tts.XFtts()
            ttsr = xftts.requestTTS(route)

            return { "result": ttsr, "aue": xftts.aue }
        else:
            return None
    def playAudio(self, ttsr):
        # 播放音频
        if not ttsr is None:
            pAudio = play.PlayAudio()
            contentType = ttsr['result'].headers['Content-Type']
            if contentType == "audio/mpeg":
                sid = ttsr['result'].headers['sid']
                if ttsr['aue'] == "raw":
                    pAudio.playAudio("audios/"+sid+".wav", ttsr['result'].content)
                else :
                    pAudio.playAudio("audios/"+sid+".mp3", ttsr['result'].content)
                print("success, sid = " + sid)
            else :
                print(ttsr['result'].text )
        else:
            print('错误：未获取到语音合成数据！')

if __name__ == '__main__':
    ma = myTherad()
    ma.start()
    ma.join()