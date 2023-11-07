import os
import time
import datetime
from moviepy.editor import *
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random


def MergeAudio(content):
    #l = [ AudioFileClip(os.path.dirname(__file__) + "\\PreData\\%s.mp3"%i) for i in content.split()]
    l = []
    for i in content.split():
        if "https://" not in i:
            l.append(AudioFileClip(os.path.dirname(__file__) + "\\PreData\\%s.mp3"%i))
    merged = CompositeAudioClip(l)
    img = ImageClip(os.path.dirname(__file__) + "\\Data\\%s_%d.png" % (date, 0))
    #img = img.duration(5.0)
    final = [img]
    out = concatenate(final,method="compose")  # .write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % date, fps=24)
    out = out.set_audio(merged)
    print(merged.duration)
    out = out.subclip(0, merged.duration)
    out.write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % date, fps=24)



def select_phrase():
    f1 = open(os.path.dirname(__file__)+"\\Start_Phrase.txt","r")
    phrase = random.choice(f1.read().split("\n"))
    print(phrase)
    f2 = open(os.path.dirname(__file__)+"\\Subscribe.txt","r")
    subphrase = random.choice(f2.read().split("\n"))
    print(subphrase)
    return (phrase,subphrase)


def ConvertText(content):
    for word in content.split():
        browser.implicitly_wait(10)
        l = os.listdir(os.path.dirname(__file__) + "\\PreData\\")
        if word+".mp3" in l:
            continue
        browser.get("https://elevenlabs.io/speech-synthesis")
        browser.find_element(By.CSS_SELECTOR, 'textarea[name="text"]').send_keys(Keys.CONTROL+"a")
        browser.find_element(By.CSS_SELECTOR, 'textarea[name="text"]').send_keys(Keys.DELETE)
        time.sleep(2)
        #l = select_phrase()
        #full_content = content+l[1]
        browser.find_element(By.CSS_SELECTOR, 'textarea[name="text"]').send_keys(word)
        time.sleep(6)
        browser.find_element(By.XPATH,'//button[text()="Generate"]').click()
        wait = WebDriverWait(browser, 100)
        wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, '//button[text()="Generating"]')))
        browser.find_element(By.XPATH, '//button[@aria-label="Download Audio"]').click()
        time.sleep(8)
        l = os.listdir(os.path.dirname(__file__) + "\\Data")
        details = {}
        for i in l:
            if ".mp3" in i:
                details[time.ctime(os.path.getmtime(os.path.dirname(__file__) + "/Data/" + i))] = i
        os.rename(os.path.dirname(__file__) + "/Data/" + details[max(details)],os.path.dirname(__file__) + "/Audio/%s.mp3" % word)
        print(details[max(details)])
# date is used for naming the files
date = "".join(str(datetime.date.today()).split("-"))

count = 0

# Initalization of web Driver
opt = Options()

# This option is used to verify the action part without starting from beginning
# opt.add_experimental_option('debuggerAddress',"localhost:1135")  # CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')

services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=opt)
browser.implicitly_wait(10)
browser.maximize_window()
f = open(os.path.dirname(__file__) + "//Data//" + date + ".txt", "r")
content = f.readlines()
content = "".join(content)
MergeAudio(content)
quit()
while True:
    try:
        f = open(os.path.dirname(__file__) + "//Data//" + date + ".txt", "r")
        content = f.readlines()
        print(content)
        for index, i in enumerate(content):
            if "https:" in i:
                content.pop(index)
        print(content)
        content = "".join(content)
        print(content)
        ConvertText(content)
    except Exception as e:
        count += 1
        if count > 5:
            print("TTS error")
            break
        print(e)
    else:
        browser.quit()
        break
