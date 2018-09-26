import threading
import time
from baiduMap import lbs
from xfyun import tts
from playAudio import play

class myTherad(threading.Thread):
    def run(self):
        # 百度地图api
        baiduLbs = lbs.Lbs()
        route = baiduLbs.getBaiDuRouteMatrix()
        if not route is None:
            # 讯飞语音api
            xftts = tts.XFtts()
            ttsr = xftts.requestTTS(route)
            # 播放音频
            pAudio = play.PlayAudio()
            contentType = ttsr.headers['Content-Type']
            if contentType == "audio/mpeg":
                sid = ttsr.headers['sid']
                if xftts.aue == "raw":
                    pAudio.playAudio("audios/"+sid+".wav", ttsr.content)
                else :
                    pAudio.playAudio("audios/"+sid+".mp3", ttsr.content)
                print("success, sid = " + sid)
            else :
                print(ttsr.text )
        """ while True:
            time.sleep(1)
            self.getBaiDuRouteMatrix() """

if __name__ == '__main__':
    ma = myTherad()
    ma.start()
    ma.join()