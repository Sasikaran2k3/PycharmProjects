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


def StartScarpingNews(page_no, page):
    f = open(os.path.dirname(__file__) + "\\Data\\newsLinks.txt", "a")
    # Link to first news is taken from a tag and stored in newsLinks.txt
    # It happens for all news urls
    # Each URL is for different Topics like tech, mobile, etc.
    browser.get(page)
    print("%d) Waiting to load... " % page_no)
    list_of_link = browser.find_element(By.CSS_SELECTOR, 'div[class="thumb"]>a')
    f.write(list_of_link.get_attribute("href") + "\n")
    f.close()


def StartScrapData():
    # Each particular news page link is taken from newsLinks.txt
    f = open(os.path.dirname(__file__) + "\\Data\\newsLinks.txt", "r")
    data = f.readlines()
    # c is count variable for naming the audio file
    c = 1
    title_selector = "div[class='lead_heading header_wrap']>h1"
    image_selector = "div[class='fullstoryImage']>div[class = 'heroimg']>img"
    description_selector = "div[class='content_text row description']>p"
    # All the links are opened one by one and title, img, descriptions are scrapped
    for link in data:
        browser.get(link)
        try:
            browser.execute_script("window.stop();")
            check = browser.find_element(By.CSS_SELECTOR, image_selector)
            title = browser.find_element(By.CSS_SELECTOR, title_selector).text
            news_description = browser.find_element(By.CSS_SELECTOR, description_selector).text
            url = check.get_attribute("src")
            time.sleep(2)
        except:
            print("img Not found")
            continue
        file = open(os.path.dirname(__file__) + "\\Data\\" + "%s.txt" % (date + str(c)), "w")
        file.write(title + " \n" + news_description + "\n" +link + "\n Check the Description for more Details")
        pic_name = os.path.dirname(__file__) + "\\Data\\" + date + str(c) + ".png"
        # wget is used to download image from its url and saves with given name
        wget.download(url, out=pic_name)
        file.close()
        c += 1


# date is used for naming the files
date = "".join(str(datetime.date.today()).split("-")) + "_"

# number of jobs are listed in queue
Queue = list(range(1, 6))

# Initalization of web Driver
opt = Options()

# This option is used to verify the action part without starting from beginning
# opt.add_experimental_option('debuggerAddress',"localhost:1135")  # CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')

services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=opt)
browser.maximize_window()
error_count = 0
# l is a list of all the files in the folder named Data
l = os.listdir(os.path.dirname(__file__) + "\\Data")
for i in l:
    # All files in Data Folder is deleted
    os.remove(os.path.dirname(__file__) + "\\Data\\" + i)
    browser.implicitly_wait(5)

# f is a text file which contain all the news web page links
f = open(os.path.dirname(__file__)  + "//NewsPageLink.txt", "r")
Links = f.readlines()
f.close()
while True:
    try:
        # Scrap news link from each page using no of works in Queue
        for i in Queue:
            StartScarpingNews(i, Links[i-1])

        # Scrap Data like img and content from news page
        StartScrapData()
    except Exception as e:
        error_count += 1
        print(e)
        if error_count > 10:
            break
    else:
        break
browser.close()

