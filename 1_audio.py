import os 
import sounddevice
import wavio
import datetime



# 오디오 캡처 및 녹음을 위한 초기 설정
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORDING_DIR = "recording"

if not os.path.exists(RECORDING_DIR):
    os.makedirs(RECORDING_DIR)

def record_audio(filename, duration):
    time = datetime.datetime.now
    