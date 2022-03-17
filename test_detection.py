import os, sys
import json
import time
import requests
import threading
from threading import Timer
from acrcloud.recognizer import ACRCloudRecognizer

import sounddevice
from scipy.io.wavfile import write

current_song_isrc = '';

def process_recognition_results(results):
    print(results)
    global current_song_isrc
    status_object = results["status"]
    # replace this with appropriate url
    url = 'https://9464-102-222-146-194.ngrok.io/songs/recognition_results/'
    headers = {
        'Content-Type': 'application/json; charset=utf8'
    }
    
    if status_object["code"] == 0:
        data = results["metadata"]["music"][0]
        current_song_isrc = data['external_ids']['isrc']
        response = requests.post(url, json.dumps(data), headers=headers)
        if response.status_code == 200:
            print("Posted successfully..")
        else:
            print("An error occured while posting...")
    else:
        print("Unrecorgnized music", status_object)
    
    

def record_audio():
    fs = 44100
    seconds = 20
    print("recording started...")
    global current_song_isrc
    record_audio = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=1)
    sounddevice.wait()
    write("samplerec.wav", fs, record_audio)
    
    print("Finished recording.")
    
    
    time.sleep(5)
    print('Analysing audio')
    
    recognizer = ACRCloudRecognizer(config)
    results = recognizer.recognize_by_file('samplerec.wav', 10)
    
    music_details = process_recognition_results(json.loads(results))
    # process results
    # send results to the backend
    print("Cleaning up files")
    time.sleep(2)
    os.remove("samplerec.wav")
    print("Finished processing")
    # calculate waiting time for the next recording
    global current_song_isrc
    temp_results = json.loads(results)
    status_object = temp_results["status"]
    
    if status_object["code"] == 0:
        data = temp_results["metadata"]["music"][0]
        current_song_isrc = data['external_ids']['isrc']
        duration = data['duration_ms']
        seo = data['sample_end_time_offset_ms']
        sbo = data['sample_begin_time_offset_ms']
        waiting_time = duration - (seo - sbo)
        waiting_time = waiting_time / 1000
        print(f'Song duration is: {duration}')
        print(f"sleeping for {waiting_time} seconds untill the song ends")
        time.sleep(waiting_time)
    
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
    
