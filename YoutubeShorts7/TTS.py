import os
import requests
import wget
import time
import datetime
import threading
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


def ConvertText(content):
    browser.get("https://ttsfree.com/")
    #browser.refresh()
    browser.find_element(By.CSS_SELECTOR, 'textarea[name="input_text"]').send_keys(content)
    act = ActionChains(browser)
    lang_select = browser.find_element(By.CSS_SELECTOR, 'span[class="selection"]')
    drop = Select(browser.find_element(By.ID, "select_lang_bin"))
    drop.select_by_value("en-IN")
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'a[title="Convert now"]').click()
    wait = WebDriverWait(browser, 100)
    wait.until(expected_conditions.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Download Mp3')))
    audio = browser.find_element(By.XPATH, '//div[@class="label_process text-left"]/audio/source[2]')
    url = str(audio.get_attribute("src"))
    print(url)
    r = requests.get(url)
    with open(os.path.dirname(__file__) + "\\Data\\" + "%s.mp3" % (date),"wb") as f:
        f.write(r.content)


# date is used for naming the files
date = "".join(str(datetime.date.today()).split("-"))

count = 0

# Initalization of web Driver
opt = Options()

# This option is used to verify the action part without starting from beginning
#opt.add_experimental_option('debuggerAddress',"localhost:1135")  # CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
opt.add_argument(r'--user-data-dir=E:\AutomationBrowser')

services = Service(executable_path=r"C:\Users\SASIKARAN\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=opt)
browser.implicitly_wait(10)
browser.maximize_window()

while True:
    try:
        # Login
        browser.get("https://ttsfree.com/login")
        browser.find_element(By.CSS_SELECTOR, 'div[class="icheckbox_square-green"]').click()
        browser.find_element(By.CSS_SELECTOR, 'input[value="Login"]').click()
        input()
        f = open(os.path.dirname(__file__) + "//Data//" + date + ".txt", "r")
        content = f.readlines()
        for index, i in enumerate(content):
            if "https:" in i:
                content.pop(index)
        content = "".join(content)
        print(content)
        ConvertText(content)
    except Exception as e:
        count += 1
        if count > 10:
            print("TTS error")
            break
        print(e)
    else:
        browser.quit()
        break
