import os, sys
import json
import time
import threading
from threading import Timer
from acrcloud.recognizer import ACRCloudRecognizer

import sounddevice
from scipy.io.wavfile import write

def process_recognition_results(results):
    status_object = results["status"]
    if status_object["code"] == 0:
        music_data = results["metadata"]["music"][0]
        title = music_data["title"]
        label = music_data["label"]
        
        album_data = music_data["album"]
        
        artists = music_data["artists"]
        
        genres = music_data["genres"]
        external_ids = music_data["external_ids"]
    else:
        print("Unrecorgnized music", json.dumps(status_object))
    
    

def record_audio():
    fs = 44100
    seconds = 20
    print("recording started...")
    record_audio = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=1)
    sounddevice.wait()
    write("samplerec.wav", fs, record_audio)
    
    print("Finished recording.")
    
    
    time.sleep(5)
    print('Analysing audio')
    
    recognizer = ACRCloudRecognizer(config)
    results = recognizer.recognize_by_file('samplerec.wav', 10)
    music_details = process_recognition_results(results)
    # process results
    # send results to the backend
    print("Cleaning up files")
    time.sleep(2)
    os.remove("samplerec.wav")
    print("Finished processing")
    
if __name__ == '__main__':
    config = {
        'host':'identify-eu-west-1.acrcloud.com',
        'access_key':'21c84e61402bb6018ac75dc8431a0528', 
        'access_secret':'CiXTw1BJmNpRPm1LhvfE6DYbNphuOKThjnNxZaSr',
        'timeout':10 # seconds
    }
    
    while True:
        record_audio()
    
    # time.sleep(2)
    # record_audio()
    # rt = RepeatedTimer(10, record_audio)
    
