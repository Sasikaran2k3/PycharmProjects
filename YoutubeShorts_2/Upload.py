import os
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

# date is used for naming the files
date = "".join(str(datetime.date.today()).split("-")) + "_"

# number of jobs are listed in queue
Queue = list(range(1, 6))

# Initalization of web Driver
opt = Options()

# This option is used to verify the action part without starting from beginning
#opt.add_experimental_option('debuggerAddress', "localhost:1135")
# CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')
services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=opt)
browser.maximize_window()
browser.implicitly_wait(10)
i = 1
f = open(os.path.dirname(__file__) + "\\chatgpt_prompt.txt", "r")
prompt = f.read()
while Queue:
    try:
        browser.get("https://chat.openai.com/")
        wait = WebDriverWait(browser,100)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[text() = 'Hashtag suggestions generated']")))
        f = open(os.path.dirname(__file__) + "/Data/" + date + str(i) +".txt","r")
        content = f.readlines()
        print(content)
        title = content[0]
        desc = content[1]
        link = content[2]
        browser.find_element(By.XPATH, "//textarea").send_keys(prompt+desc)
        gpt_result = browser.find_elements(By.XPATH, '//div[@class="markdown prose w-full break-words dark:prose-invert light"]//li')
        yt_hashtags = " ".join([i.text for i in gpt_result])
        print(yt_hashtags)
        browser.find_element(By.XPATH, '//button[@class="p-1 hover:text-white"][3]').click()
        browser.find_element(By.XPATH, '//div[@class="absolute flex right-1 z-10 text-gray-300 visible"]/button[1]').click()
        time.sleep(10)
        # Open Yt Studio
        browser.get("https://studio.youtube.com/")

        # Create Button
        browser.find_element(By.ID, "create-icon").click()
        browser.find_element(By.ID, "text-item-0").click()
        data = os.path.dirname(__file__) + "/Data/" + date + str(i) + ".mp4"
        browser.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(data)
        print(title,"\n\n",desc)
        text_boxes = browser.find_elements(By.CSS_SELECTOR, 'div[id="textbox"]')
        text_boxes[0].clear()
        text_boxes[0].send_keys(title)
        text_boxes[1].clear()
        text_boxes[1].send_keys(desc+link+yt_hashtags)
        browser.find_element(By.XPATH, '//tp-yt-paper-radio-button[@class="style-scope ytkc-made-for-kids-select"][2]').click()
        browser.find_element(By.XPATH, '//div[text() = "Next"]').click()
        browser.find_element(By.XPATH, '//div[text() = "Next"]').click()
        browser.find_element(By.XPATH, '//div[text() = "Publish"]').click()
        time.sleep(10)
        i += 1
        Queue.pop(0)
        print(Queue)
    except Exception as e:
        print(e)
    else:
        break