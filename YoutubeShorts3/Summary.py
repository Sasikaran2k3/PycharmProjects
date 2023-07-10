import os
import wget
import time
import datetime
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
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
        browser.get("https://quillbot.com/")
        time.sleep(2)

        browser.find_element(By.XPATH,'//div[@class="MuiBox-root css-9zwoh9"]').send_keys(data[0])
        time.sleep(3)
        browser.find_element(By.XPATH,'//div[text() = "Paraphrase"] ').click()

        wait = WebDriverWait(browser,100)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//div[text()="Rephrase"]')))
        time.sleep(10)

        new_title = browser.find_element(By.XPATH, '//div[@id="paraphraser-output-box"]').text
        print(new_title)

        assert data[0] != new_title

        browser.get("https://quillbot.com/")
        time.sleep(2)

        browser.find_element(By.XPATH,'//div[@class="MuiBox-root css-9zwoh9"]').send_keys(data[1])
        time.sleep(3)
        browser.find_element(By.XPATH,'//div[text() = "Paraphrase"] ').click()

        wait = WebDriverWait(browser,100)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//div[text()="Rephrase"]')))
        time.sleep(10)

        new_desc = browser.find_element(By.XPATH, '//div[@id="paraphraser-output-box"]').text
        print(new_desc)

        assert data[0] != new_desc

        output = [new_title+"\n", new_desc+"\n", data[2],data[3]]
        print(output)

        f = open(os.path.dirname(__file__)+"/Data/"+date+".txt",'w')
        f.writelines(output)
        f.close()
    except Exception as e:
        count += 1
        if count > 10:
            print("Error Limit Reached")
            break
        print(e)
    else:
        browser.quit()
        break