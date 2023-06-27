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
browser.implicitly_wait(5)
count = 0
# l is a list of all the files in the folder named Data
l = os.listdir(os.path.dirname(__file__) + "\\Data")
for i in l:
    # All files in Data Folder is deleted
    os.remove(os.path.dirname(__file__) + "\\Data\\" + i)
    browser.implicitly_wait(5)

# f is a text file which contain all the news web page links
f = open(os.path.dirname(__file__)  + "//NewsPageLink.txt", "r+")
f.seek(0)
Links = f.readlines()
today_link = Links.pop(0)
Links.append(today_link)
f.seek(0)
f.writelines(Links)
while True:
    try:
        browser.get(today_link)

        page = browser.find_element(By.CSS_SELECTOR, 'div[class="thumb"]>a')
        link = page.get_attribute("href")
        page.click()

        title_selector = "div[class='lead_heading header_wrap']>h1"
        image_selector = "div[class='fullstoryImage']>div[class = 'heroimg']>img"
        description_selector = "div[class='content_text row description']>p"
        check = browser.find_element(By.CSS_SELECTOR, image_selector)
        title = browser.find_element(By.CSS_SELECTOR, title_selector).text
        news_description = browser.find_element(By.CSS_SELECTOR, description_selector).text
        url = check.get_attribute("src")
        browser.quit()
        time.sleep(2)
        file = open(os.path.dirname(__file__) + "\\Data\\" + "%s.txt" % (date), "w")
        file.write(title + " \n" + news_description + "\n" +link + "\n Check the Description for more Details")
        pic_name = os.path.dirname(__file__) + "\\Data\\" + date + ".png"
        # wget is used to download image from its url and saves with given name
        wget.download(url, out=pic_name)
        file.close()
    except Exception as e:
        print(e)
        count += 1
        if count > 5 :
            print("Scrap Error")
            break
    else:
        browser.quit()
        print("\nScrap Successful\n")
        break


