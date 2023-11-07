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
        input()
        time.sleep(2)
        browser.find_element(By.XPATH, '//button[@aria-controls="tabs--panel--2"]').click()
        clear = browser.find_elements(By.XPATH, '//button[@class="_clear_1qglh_173"]')
        if clear !=[]:
            clear[0].click()
            browser.switch_to.alert.accept()
        wait = WebDriverWait(browser,1000)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//p[text()="Start chatting now!"]')))
        prompt = data[0].replace("\n", "") + ".write a 30 seconds audio script for youtube shorts with this title. \n"
        print("prompt :",prompt)
        browser.find_element(By.XPATH, '//input[@placeholder="Enter your message..."]').send_keys(prompt)
        time.sleep(10)
        chat = browser.find_elements(By.XPATH,'// div[ @class ="_item_nop3r_1 _bot_nop3r_35"]')
        print(len(chat))
        dialogs = chat[0].find_elements(By.XPATH,"//p")
        for i in dialogs:
            dialog = i.text
            if "Rytr" not in dialog or "[" not in dialog:
                print(dialog)
        new_title = browser.find_elements(By.XPATH, '//p[@dir="auto"]')[-1].text
        print(new_title)
        output = [new_title + "\n", data[1]]
        print(output)
        input()
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