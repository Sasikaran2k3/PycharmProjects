import time
import os
import pyautogui as py
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

def Initialize():
    opt = Options()
    opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')
    services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
    global browser
    browser = Chrome(service=services, options=opt)
    browser.maximize_window()


def putOnEditor():
    browser.get("https://www.kapwing.com/studio/editor/subtitles")
    py.moveTo(1080, 380)  # Click To upload Button
    py.click()
    time.sleep(4)
    py.write(os.getcwd() + "\\Data\\" + "0.mp4\n")


def startToEdit():
    py.moveTo(1180, 250)  # Click To Resize Button
    py.click()
    py.moveTo(690, 305)  # Click To 9:16 Ratio Canvas
    py.click()
    browser.find_element(By.CSS_SELECTOR, 'button[class="ResizeCanvas-module_primaryButton_lCNbg"]').click()

    browser.find_element(By.CSS_SELECTOR, '#mediaSidebarControls > div.MediaSidebar-module_mediaSidebarControlContent_Wp6-t > div > div.Tabs-module_tabContent_Uom4r.Tabs-module_noBottomPadding_yGGq6 > div:nth-child(7) > div.MagicSubtitlesTab-module_notificationAction_h072z').click()
    browser.find_element(By.CSS_SELECTOR,'button[class="TranscribeButton-module_button_wVi5t undefined"]').click()
    browser.find_element(By.CSS_SELECTOR, 'button[class="Transcribe-module_transcribeButton_5yp6Z"]').click()
