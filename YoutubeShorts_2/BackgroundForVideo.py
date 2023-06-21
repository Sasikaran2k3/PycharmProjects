import time
import os
import datetime
import requests
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


def MakeVideo():
    for i in Queue:
        print(os.path.dirname(__file__) + "\\Data\\%s.mp3" % (date+str(i)))
        audio = AudioFileClip(os.path.dirname(__file__) + "\\Data\\%s.mp3" % (date+str(i)))
        back = AudioFileClip(os.path.dirname(__file__) + "\\Background.mp3")
        image = ImageClip(os.path.dirname(__file__) + "\\Data\\%s.png" % (date+str(i)))
        video = image.set_audio(CompositeAudioClip([audio,back]))
        audio_duration = audio.duration + 1
        video.duration = audio_duration
        video = video.subclip(0, audio_duration)
        video.fps = 1
        video.write_videofile(os.path.dirname(__file__) + "\\Data\\%s.mp4" % (str(i)))


def putOnEditor():
    browser.implicitly_wait(10)
    # Count finds no of times error happens and if count is more than 10, Program stops
    count = 0
    j = 1
    # Queue is list of tasks of 5 videos
    Queue = list(range(1, 6))
    while True:
        try:
            while Queue != []:
                browser.get("https://www.kapwing.com/folder/")
                browser.find_element(By.XPATH, '//div[@data-cy="workspace-new-project-button"]').click()
                browser.find_element(By.XPATH, '//div[text() = "Create a New Project"]').click()
                browser.find_element(By.XPATH, '//input[@data-cy="upload-input"]').send_keys(
                    os.path.dirname(__file__) + "\\Data\\" + "%d.mp4" % j)
                time.sleep(10)
                wait = WebDriverWait(browser, 100)
                # Wait till the upload symbol gets invisible
                wait.until(expected_conditions.invisibility_of_element(
                    (By.XPATH, '//img[@src="/assets/pending-media-upload-icon.e21cbd1d.gif"]')))

                print("Video  Imported")
                ActionChains(browser).send_keys(Keys.ESCAPE).perform()
                browser.find_element(By.XPATH, '//div[@data-cy="resize-canvas-button"]').click()
                browser.find_element(By.XPATH, '//div[@data-cy="916-small-control-button"][1]').click()
                browser.find_element(By.XPATH, '//button[@data-cy="resize-apply"]').click()
                browser.find_element(By.XPATH, '//div[text() = "Subtitles"]').click()
                time.sleep(2)
                browser.find_element(By.XPATH,
                                     '//button[@class="MagicSubtitleStart-module_primaryButton_uyrZz"]').click()
                time.sleep(8)
                print("Start Transcribing")
                wait.until(expected_conditions.presence_of_element_located(
                    (By.XPATH, 'textarea[data-cy="magic-textarea"]')))
                print("Selecting Style")
                time.sleep(2)
                browser.find_element(By.XPATH, '//div[@class="Track-module_container_mph21"][1]').click()
                time.sleep(5)
                browser.find_element(By.CSS_SELECTOR, 'textarea[data-cy="magic-textarea"]').click()
                print("Changing Position")
                act = ActionChains(browser)
                transform = browser.find_elements(By.XPATH, '//div[@data-cy="drag-handler"]')
                # moves the subtitle from the video bottom left position
                act.click_and_hold(transform[1]).move_to_element_with_offset(transform[0], 90, 120)
                act.release().perform()
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
                wait.until(expected_conditions.visibility_of_element_located(
                    (By.XPATH, '//div[@class="VideoContainer-module_commentsMetaDataFileSize_E7zW4"]')))
                url = browser.find_element(By.XPATH, '//video[@id="final-video"]').get_attribute("src")
                print("\n", url, "\n")
                r = requests.get(url)
                with open(os.path.dirname(__file__) + "\\Data\\" + "%s.mp4" % (date + str(j)), "wb") as f:
                    f.write(r.content)

                j += 1
                Queue.pop(0)
                print(Queue)
        except Exception as e:
            count += 1
            print("Error Encountered")
            print("Error Count : %d" % count)
            print(e)
            browser.refresh()
            if count > 10:
                break
        else:
            break
    time.sleep(50)
    print("Completed Successfully")
    browser.close()


def demo():
    browser.implicitly_wait(5)
    browser.get("https://www.kapwing.com/folder/")
    browser.find_element(By.XPATH, '//div[@data-cy="workspace-new-project-button"]').click()
    browser.find_element(By.XPATH, '//div[text() = "Create a New Project"]').click()


# date is used for naming the files
date = "".join(str(datetime.date.today()).split("-")) + "_"

opt = Options()
# This option is used to verify the action part without starting from beginning
opt.add_experimental_option('debuggerAddress', "localhost:1135") #CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')
services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=opt)
browser.maximize_window()
Queue = list(range(1,6))
#demo()
#MakeVideo()
putOnEditor()