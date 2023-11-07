import os
import time
import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys



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
data = f.readlines()

count = 0

while True:
    try:
        # Rytr Ai
        browser.get("https://app.rytr.me/create")
        time.sleep(2)
        browser.find_element(By.XPATH, '//button[@aria-controls="tabs--panel--2"]').click()
        prompt = data[0].replace("\n", "") + ". This is a news title, shorten this into 2 sentence for MEME with emotion triggering or personally relatable words and first sentence can strictly have less than 100 characters ONLY\n"
        print("prompt :",prompt)
        browser.find_element(By.XPATH, '//input[@placeholder="Enter your message..."]').send_keys(prompt)
        time.sleep(10)
        new_title = browser.find_elements(By.XPATH, '//p[@dir="auto"]')[-1].text
        print(new_title)
        output = [new_title + "\n", data[1]]
        print(output)

        f = open(os.path.dirname(__file__) + "/Data/" + date + ".txt", 'w')
        f.writelines(output)
        f.close()
    except Exception as e:
        count += 1
        if count > 2:
            print("Error Limit Reached")
            break
        print(e)
    else:
        browser.quit()
        break