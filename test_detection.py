import os, sys
import time
from acrcloud.recognizer import ACRCloudRecognizer

import sounddevice
from scipy.io.wavfile import write

def record_audio():
    fs = 44100
    seconds = 20
    print("recording started...")
    record_audio = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=1)
    sounddevice.wait()
    write("samplerec.wav", fs, record_audio)
    
    print("Finished...")

if __name__ == '__main__':
    config = {
        'host':'identify-eu-west-1.acrcloud.com',
        'access_key':'21c84e61402bb6018ac75dc8431a0528', 
        'access_secret':'CiXTw1BJmNpRPm1LhvfE6DYbNphuOKThjnNxZaSr',
        'timeout':10 # seconds
    }
    
    time.sleep(2)
    record_audio()
    time.sleep(2)
    print('Analysing audio')
    
    re = ACRCloudRecognizer(config)
    print(re.recognize_by_file('samplerec.wav', 10))