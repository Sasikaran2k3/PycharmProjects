import time
import os
import datetime
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


opt = Options()
# This option is used to verify the action part without starting from beginning
opt.add_experimental_option('debuggerAddress', "localhost:1135") #CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')
services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=opt)
browser.maximize_window()
browser.implicitly_wait(10)

def summa():
    """browser.get("https://www.kapwing.com/folder/")
    browser.find_element(By.XPATH, '//div[@data-testid="ws-header-email-container"]').click()
    browser.find_element(By.XPATH, '//div[text()="Sign Out"]').click()"""
    browser.get("https://tempmailo.com/")
    browser.find_element(By.XPATH, '//span[text()="Change"]').click()
    browser.find_element(By.XPATH, '//div[@class="text-right"]/button[1]').click()
    browser.find_element(By.XPATH, '//button[@class="iconx"]').click()
    browser.find_element(By.XPATH, '//button[@class="iconx"]').click()
    browser.get("https://www.kapwing.com/signin")
    browser.find_element(By.XPATH, '//input[@type = "email"]').click()
    act = ActionChains(browser)
    act.key_down(Keys.CONTROL).key_down("v").perform()
    browser.find_element(By.XPATH,'//button[text()="Continue with email"]').click()
    time.sleep(5)
    browser.get("https://tempmailo.com/")
    browser.find_element(By.XPATH,'//div[text()=\'"Kapwing" <no-reply@kapwing.com>\']').click()
print(browser.find_element(By.XPATH,'//div[@class="code"]').text)
browser.find_element(By.XPATH,'//body')