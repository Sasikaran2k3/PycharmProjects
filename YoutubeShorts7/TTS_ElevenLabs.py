import os
import time
import datetime
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random

def ConvertText(content):
    browser.get("https://elevenlabs.io/speech-synthesis")
    input()
    browser.find_element(By.CSS_SELECTOR, 'textarea[name="text"]').send_keys(Keys.CONTROL+"a")
    browser.find_element(By.CSS_SELECTOR, 'textarea[name="text"]').send_keys(Keys.DELETE)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, 'textarea[name="text"]').send_keys(content)
    time.sleep(2)
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
    os.rename(os.path.dirname(__file__) + "/Data/" + details[max(details)],os.path.dirname(__file__) + "/Data/%s.mp3" % date)
    print(details[max(details)])
# date is used for naming the files
date = "".join(str(datetime.date.today()).split("-"))

count = 0

# Initalization of web Driver
opt = Options()

# This option is used to verify the action part without starting from beginning
# opt.add_experimental_optio#opt.add_experimental_option('debuggerAddress',"localhost:1135")  # CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\AutomationBrowser"
opt.add_argument(r'--user-data-dir=E:\UpgradeBuddy')

services = Service(executable_path=r"C:\Users\SASIKARAN\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=opt)
browser.implicitly_wait(10)
browser.maximize_window()


while True:
    try:
        f = open(os.path.dirname(__file__) + "//Data//" + date + "_script.txt", "r")
        content = f.readlines()
        print(content)
        stripped_content = ""
        for i in content:
            stripped_content += i.strip()+"\n"
        print(stripped_content)
        ConvertText(stripped_content)
    except Exception as e:
        count += 1
        if count > 5:
            print("TTS error")
            break
        print(e)
    else:
        browser.quit()
        break
