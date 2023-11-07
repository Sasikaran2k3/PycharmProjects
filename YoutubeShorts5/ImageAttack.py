import os
import wget
import time
import datetime

from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.concatenate import concatenate
from moviepy.video.fx.fadeout import fadeout
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



# date is used for naming the files
date = "".join(str(datetime.date.today()).split("-"))


# Initalization of web Driver
opt = Options()

# This option is used to verify the action part without starting from beginning
#opt.add_experimental_option('debuggerAddress',"localhost:1135")  # CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')

services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=opt)
browser.maximize_window()
browser.implicitly_wait(15)

f = open(os.path.dirname(__file__)+"/Data/"+date+".txt",'r')
data = f.read().split()
c = 0
for i in data:
    if len(i) > 2:
        browser.get("https://www.google.com/imghp")
        browser.find_element(By.XPATH, "//textarea[@type='search']").click()
        browser.find_element(By.XPATH, "//textarea[@type='search']").send_keys(i + "\n")
        all_img = browser.find_elements(By.XPATH, '//div[@class="fR600b islir"]//img')
        for j in all_img:
            j.click()
            time.sleep(4)
            url = browser.find_elements(By.XPATH, '//div[@class="MAtCL PUxBg"]//img')
            pic_name = os.path.dirname(__file__) + "\\Data\\" + date + "_%s" % i + ".png"
            for k in url:
                if "http" in k.get_attribute("src"):
                    j.screenshot(pic_name)
                    print("downloaded")
                    c += 1
                    break
            break
quit()
date = "".join(str(datetime.date.today()).split("-"))
audio = AudioFileClip(os.path.dirname(__file__) + "\\Data\\%s.mp3" % date)
back = AudioFileClip(os.path.dirname(__file__) + "\\Background.mp3")
print(c)
#img1 = ImageClip(os.path.dirname(__file__) + "\\Data\\%s.png" % date).set_duration(divider)
final = []
for i in range(c):
    pic_num = i
    img = ImageClip(os.path.dirname(__file__) + "\\Data\\%s_%d.png" % (date, pic_num))
    img = img.resize(height=1080, width=1920)
    img = img.set_duration(divider)
    if i != 0:
        img = fadeout(img, 1)
    final .append(img)
out = concatenate(final, method="compose")#.write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % date, fps=24)
out = out.set_audio(CompositeAudioClip([audio, back]))
out.duration = divider*shift_count + 0.5
print(out.duration)
out_len = divider*shift_count + 0.5
out = out.subclip(0, out_len)
out.write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % date, fps=24)
browser.maximize_window()
"""
audio = AudioFileClip(os.path.dirname(__file__) + "\\Data\\%s.mp3" % date)
back = AudioFileClip(os.path.dirname(__file__) + "\\Background.mp3")
image = ImageClip(os.path.dirname(__file__) + "\\Data\\%s.png" % date)
video = image.set_audio(CompositeAudioClip([audio, back]))
audio_duration = audio.duration + 1
video.duration = audio_duration
video = video.subclip(0, audio_duration)
video.fps = 1
video.write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % date)
"""
count = 0
