import time
import os
import datetime
from moviepy.editor import *
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video import VideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.fx.fadeout import fadeout
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import pyautogui as py


# date is used for naming the files
date = "".join(str(datetime.date.today()).split("-"))

opt = Options()
# This option is used to verify the action part without starting from beginning
#opt.add_experimental_option('debuggerAddress', "localhost:1135") #CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')
services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=opt)
browser.implicitly_wait(10)

# Merge Audio and Video


date = "".join(str(datetime.date.today()).split("-"))
audio = AudioFileClip(os.path.dirname(__file__) + "\\Data\\%s.mp3" % date)
back = AudioFileClip(os.path.dirname(__file__) + "\\TimeTick.mp3")
shift_count = 5
divider = audio.duration / shift_count
#img1 = ImageClip(os.path.dirname(__file__) + "\\Data\\%s.png" % date).set_duration(divider)
final = []
for i in range(shift_count):
    pic_num = i%4
    print(pic_num)
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
# Delete Old final video
l = os.listdir(os.path.dirname(__file__))
for i in l:
    if ".mp4" in i:
        os.remove(os.path.dirname(__file__) + "\\" + i)

count = 0
while True:
    try:
        # Start to Edit
        browser.get("https://www.kapwing.com/folder/")
        browser.find_element(By.XPATH, '//div[@data-cy="workspace-new-project-button"]').click()
        browser.find_element(By.XPATH, '//div[text() = "Create a New Project"]').click()
        browser.find_element(By.XPATH, '//input[@data-cy="upload-input"]').send_keys(
            os.path.dirname(__file__) + "\\Data\\" + "%s.mp4" % date)
        print("Video Sent")
        time.sleep(10)
        wait = WebDriverWait(browser, 1000)
        ActionChains(browser).send_keys(Keys.ESCAPE).perform()
        browser.find_element(By.XPATH, '//div[@data-cy="resize-canvas-button"]').click()
        browser.find_element(By.XPATH, '//div[@data-cy="916-small-control-button"][1]').click()
        browser.find_element(By.XPATH, '//button[@data-cy="resize-apply"]').click()
        print("Resized")
        browser.find_element(By.XPATH, '//div[text() = "Subtitles"]').click()
        browser.find_element(By.XPATH, '//span[text() = "Auto subtitles"]').click()
        while browser.find_elements(By.XPATH, '//span[text() = "Auto Subtitle"]'):
            browser.find_element(By.XPATH, '//span[text() = "Auto Subtitle"]').click()
        print("Waiting in Subtitle")
        wait.until(expected_conditions.invisibility_of_element((By.XPATH,"//span[text()='Generating Subtitles...']")))
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//textarea[@data-cy="magic-textarea"]')))
        print("Sub Ready")
        browser.find_element(By.XPATH, '//textarea[@data-cy="magic-textarea"]').click()
        act = ActionChains(browser)
        transform = browser.find_elements(By.XPATH, '//div[@data-cy="drag-handler"]')
        # moves the subtitle from the video bottom left position
        #act.click_and_hold(transform[1]).move_to_element_with_offset(transform[0], 85, 128)
        #act.release().perform()
        parent = browser.find_elements(By.XPATH, '//div[@class="PresetPreview-module_container_034hO"]')
        # selects the subtitle style
        for i in parent:
            if i.find_element(By.TAG_NAME, 'input').get_attribute("value") == "My":
                i.click()
                break
        browser.find_element(By.CSS_SELECTOR, 'div[data-cy="create-button"]').click()

        browser.find_element(By.CSS_SELECTOR, 'div[data-cy="export-panel-create-button"]').click()
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,
                             'div[class = "common-module_smallControlButton_66vuT ExportRow-module_buttonStyle_L6WYa ExportRow-module_studioColor_ltubC "]').click()
        time.sleep(7)
        print("Download Page")
        # Waits till the size of the file appears and then dowload button is clicked
        wait = WebDriverWait(browser, 1000)
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//div[@class="VideoContainer-module_commentsMetaDataFileSize_E7zW4"]')))
        browser.find_element(By.XPATH, '//button[@data-cy="download-final-video-button"]').click()
        time.sleep(20)
        l = os.listdir(os.path.dirname(__file__) + "\\Data")
        details = {}
        for i in l:

            if ".mp4" in i:
                details[time.ctime(os.path.getmtime(os.path.dirname(__file__)+"/Data/" + i))] = i
        os.rename(os.path.dirname(__file__)+"/Data/"+details[max(details)],os.path.dirname(__file__)+"/%s.mp4" % date)
        #os.rename(os.path.dirname(__file__) + "/Data/" + details[max(details)],os.path.dirname(__file__) +"/Output/%s.mp4" % date)
        print(details[max(details)])
    except Exception as e:
        print(e)
        count += 1
        if count > 10:
            print("Kapwing Error")
            break
    else:
        browser.quit()
        break