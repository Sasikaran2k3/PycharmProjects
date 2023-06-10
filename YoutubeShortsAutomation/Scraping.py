import time

from PIL import Image
import os
import wget
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def Initialize():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
    global browser
    browser = Chrome(service=services)
    l = os.listdir(os.path.dirname(__file__) + "\\Data")
    for i in l:
        os.remove(os.path.dirname(__file__) + "\\Data\\" + i)
    browser.implicitly_wait(5)


def StartScarpingNews():
    # Grabs news web pages url and stored as pages
    with open(os.path.dirname(__file__) + "\\NewsPageLink.txt", "r") as pages:
        f = open(os.path.dirname(__file__) + "\\Data\\newsLinks.txt", "w")
        # Link to first news is taken from a tag and stored in newsLinks.txt
        # It happens for all news urls
        # Each URL is for different Topics like tech, mobile, etc.
        for page in pages.readlines():
            browser.get(page)
            print("Waiting to load... ")
            list_of_link = browser.find_element(By.CSS_SELECTOR, 'div[class="thumb"]>a')
            f.write(list_of_link.get_attribute("href") + "\n")
        f.close()


def StartScrapData():
    # Each particular news page link is taken from newsLinks.txt
    f = open(os.path.dirname(__file__) + "\\Data\\newsLinks.txt", "r")
    data = f.readlines()
    # c is count variable for naming the audio file
    c = 0
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
        file = open(os.path.dirname(__file__) + "\\Data\\" + "%s.txt" % c, "w")
        file.write(title + " \n" + news_description + "\n Check the Description for more Details")
        pic_name = os.path.dirname(__file__) + "\\Data\\" + str(c) + ".png"
        # wget is used to download image from its url and saves with given name
        wget.download(url, out=pic_name)
        file.close()
        c += 1

    browser.quit()
