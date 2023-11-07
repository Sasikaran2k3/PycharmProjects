import datetime
import os

import requests
from pydub import AudioSegment


date = "".join(str(datetime.date.today()).split("-"))
API_TOKEN = "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"

API_URL = "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        path = os.path.dirname(__file__) + "\\Data\\%s.mp3" % date
        with open(path,"wb") as f:
            f.write(response.content)
    else:
        print("error")

def Mp3Convert():
    path = os.path.dirname(__file__) + "/Data/%s" % date
    print(path+".flac")
    flac = AudioSegment.from_file(path+".flac", format="flac")
    flac.export(path+".mp3", format="mp3")


query({"inputs": "Huawei Nova 11 SE With Snapdragon 680 SoC, 4,500mAH Battery Launched",})


