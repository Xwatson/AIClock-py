import os
import pyaudio
import wave

class PlayAudio():
    chunk = 1024
    def playAudio(self, file, content):
        with open(file, 'wb') as f:
            f.write(content)
        f.close()
        f = wave.open(file, "rb")
        p = pyaudio.PyAudio()
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
				channels = f.getnchannels(),
				rate = f.getframerate(),
				output = True)
        data = f.readframes(self.chunk)
        #paly stream
        while len(data) > 0:
            stream.write(data)
            data = f.readframes(self.chunk)

        #stop stream
        stream.stop_stream()
        stream.close()
        #close PyAudio
        p.terminate()
        if os.path.exists(file):
            os.remove(file)