import os
import wget
import time
import datetime
import pyautogui
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
#opt.add_experimental_option('debuggerAddress', "localhost:1135")
# CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')
services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=opt)
browser.maximize_window()
browser.implicitly_wait(10)

f = open(os.path.dirname(__file__) + "\\chatgpt_prompt.txt", "r")
prompt = f.read()
count = 0
while True:
    try:
        browser.get("https://app.ritetag.com/hashtag-suggestions")
        browser.find_element(By.XPATH, '//button[text()="Clear"]').click()
        browser.find_element(By.XPATH, '//input[@type="file"]').send_keys(os.path.dirname(__file__) + "/Data/" + date +".png")

        f = open(os.path.dirname(__file__) + "/Data/" + date +".txt","r")
        content = f.readlines()
        print(content)
        title = content[0]
        desc = content[1]
        link = content[2]

        ActionChains(browser).click(browser.find_element(By.XPATH, "//textarea")).send_keys(title+desc).perform()
        browser.find_element(By.XPATH, '//span[text()="Suggest Hashtags"]').click()
        time.sleep(10)
        hash_result = browser.find_elements(By.XPATH, '//ul[@class="ti-tags"]//span')
        my_hash = " #upgradebuddy #technology #gadget #gadgetnews "
        yt_hashtags = " ".join(["#"+i.text for i in hash_result]) + my_hash
        print(yt_hashtags)

        # Open Yt Studio
        browser.get("https://studio.youtube.com/")

        # Create Button
        browser.find_element(By.ID, "create-icon").click()
        browser.find_element(By.ID, "text-item-0").click()
        data = os.path.dirname(__file__) + "/" + date + ".mp4"
        print(data)
        browser.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(data)
        print(title,"\n\n",desc)
        text_boxes = browser.find_elements(By.CSS_SELECTOR, 'div[id="textbox"]')
        time.sleep(10)
        text_boxes[0].clear()
        text_boxes[0].send_keys(title)
        text_boxes[1].clear()
        text_boxes[1].send_keys(desc+link+yt_hashtags)
        browser.find_element(By.XPATH, '//tp-yt-paper-radio-button[@class="style-scope ytkc-made-for-kids-select"][2]').click()
        browser.find_element(By.XPATH, '//div[text() = "Next"]').click()
        browser.find_element(By.XPATH, '//div[text() = "Next"]').click()
        browser.find_element(By.XPATH, '//div[text() = "Next"]').click()
        browser.find_element(By.XPATH, '//div[text() = "Publish"]').click()
        time.sleep(10)
        browser.implicitly_wait(25)
        data = os.path.dirname(__file__) + "/" + date + ".mp4"
        browser.get("https://www.instagram.com/")
        browser.find_element(By.CSS_SELECTOR, 'svg[aria-label="New post"]').click()
        browser.find_element(By.XPATH, '//button[text()="Select from computer"]').click()
        time.sleep(5)
        pyautogui.typewrite(data.replace("/", '\\')+"\n")
        browser.find_element(By.CSS_SELECTOR, 'svg[aria-label="Select crop"]').click()
        browser.find_element(By.CSS_SELECTOR, 'svg[aria-label="Crop portrait icon"]').click()
        browser.find_element(By.XPATH, '//div[text()="Next"]').click()
        time.sleep(3)
        browser.find_element(By.XPATH, '//div[text()="Next"]').click()
        print(desc+link+yt_hashtags)
        act = ActionChains(browser)
        act.move_to_element((browser.find_element(By.XPATH, '//div[@aria-label="Write a caption..."]'))).perform()
        act.double_click()
        #act.click((browser.find_element(By.XPATH, '//div[@aria-label="Write a caption..."]'))).perform()
        act.send_keys(desc+link+my_hash)
        act.perform()
        """for i in desc+link+yt_hashtags:
            browser.find_element(By.XPATH, '//div[@aria-label="Write a caption..."]').send_keys(i)"""
        time.sleep(10)
        browser.find_element(By.XPATH, '//div[text()="Share"]').click()
        wait = WebDriverWait(browser,1000)
        wait.until(expected_conditions.invisibility_of_element((By.XPATH, '//div[text()="Sharing"]')))
        time.sleep(5)
    except Exception as e:
        print(e)
        print(count)
        count += 1
        if count > 2:
            break
    else:
        print("Published Successfully")
        browser.quit()
        break
