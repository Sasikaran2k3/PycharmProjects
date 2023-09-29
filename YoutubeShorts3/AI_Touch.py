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
        prompt = data[0].replace("\n", "") + "optimise the headline for youtube shorts title with seo keywords and more attractive words gwithin 100 characters ONLY\n"
        print("prompt :",prompt) #. This is a news title, shorten this into 2 sentence for. This is a news title, shorten this into 2 sentence for MEME
        browser.find_element(By.XPATH, '//input[@placeholder="Enter your message..."]').send_keys(prompt)
        time.sleep(10)
        new_title = browser.find_elements(By.XPATH, '//p[@dir="auto"]')[-1].text
        print(new_title)
        # Quill Bot
        browser.get("https://quillbot.com/")
        time.sleep(2)
        pop_up_ad = browser.find_elements(By.XPATH, '//div[@data-testid="action-icon-button"]')
        if len(pop_up_ad) == 2:
            pop_up_ad[1].click()
        browser.find_element(By.XPATH, '//div[@role="textbox"]').send_keys(data[1])
        time.sleep(3)
        browser.find_element(By.XPATH, '//div[text() = "Paraphrase"] ').click()

        wait = WebDriverWait(browser, 100)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//div[text()="Rephrase"]')))
        time.sleep(10)

        new_desc = browser.find_element(By.XPATH, '//div[@id="paraphraser-output-box"]').text
        print(new_desc)

        assert data[1] != new_desc

        output = [new_title + "\n", new_desc + "\n", data[2], data[3]]
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