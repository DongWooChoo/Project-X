import pyaudio
import wave
from playsound import playsound
from datetime import datetime
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
RECORD_SECONDS = 15
now = datetime.now()
name = str(now.year) + str(now.month) + str(now.day) + '-' + str(now.hour) + str(now.minute) + str(now.second)
WAVE_OUTPUT_FILENAME = r'{}.wav'.format(name)

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print('음성녹음을 시작합니다.')

frames = []

for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
    data = stream.read(CHUNK, exception_on_overflow=False)
    frames.append(data)
    
print('음성녹음을 완료하였습니다.')

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print('녹음된 파일을 재생합니다.')
playsound(WAVE_OUTPUT_FILENAME)