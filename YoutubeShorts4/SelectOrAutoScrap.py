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

# date is used for naming the fi    les
date = "".join(str(datetime.date.today()).split("-"))

def additional_images(img_desc,flag = 0):
    #img_desc = "The ruling could require Apple to allow developers to provide external payment options"
    browser.get("https://www.google.com/imghp")
    browser.find_element(By.XPATH, "//textarea[@type='search']").click()
    browser.find_element(By.XPATH, "//textarea[@type='search']").send_keys(img_desc + "\n")
    all_img = browser.find_elements(By.XPATH, '//div[@class="fR600b islir"]//img')
    c = 1 if flag == 0 else 0
    for i in all_img:
        i.click()
        time.sleep(4)
        url = browser.find_elements(By.XPATH, '//div[@class="p7sI2 PUxBg"]//img')
        pic_name = os.path.dirname(__file__) + "\\Data\\" + date + "_%d" % c + ".png"
        for j in url :
            try:
                j.screenshot(pic_name)
                print("downloaded")
                c += 1
                break
            except:
                continue
        if c == 4:
            break


def select_scrap():
    count = 0
    while True:
        try:
            today_link = sugg[0]
            link = sugg[0]
            my_preference.truncate(0)
            browser.get(today_link)
            title_selector = "div[class='lead_heading header_wrap']>h1"
            image_selector = "div[class='fullstoryImage']>div[class = 'heroimg']>img"
            check = browser.find_element(By.CSS_SELECTOR, image_selector)
            title = browser.find_element(By.CSS_SELECTOR, title_selector).text
            url = check.get_attribute("src")
            img_desc = browser.find_element(By.XPATH, '//p[@class="caption"]').text
            additional_images(img_desc)
            browser.quit()
            time.sleep(2)
            file = open(os.path.dirname(__file__) + "\\Data\\" + "%s.txt" % (date), "w")
            file.write(title + " \n" + link )
            pic_name = os.path.dirname(__file__) + "\\Data\\" + date + "_0.png"
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

def auto_scrape():
    count = 0
    # f is a text file which contain all the news web page links
    f = open(os.path.dirname(__file__)  + "//NewsPageLink.txt", "r+")
    f.seek(0)
    Links = f.readlines()
    today_link = Links.pop(0)
    Links.append(today_link)
    f.seek(0)
    f.writelines(Links)
    f.close()
    while True:
        try:
            browser.get(today_link)
            page = browser.find_element(By.CSS_SELECTOR, 'div[class="thumb"]>a')
            link = page.get_attribute("href")
            page.click()
            title_selector = "div[class='lead_heading header_wrap']>h1"
            image_selector = "div[class='fullstoryImage']>div[class = 'heroimg']>img"
            check = browser.find_element(By.CSS_SELECTOR, image_selector)
            title = browser.find_element(By.CSS_SELECTOR, title_selector).text
            img_desc = browser.find_element(By.XPATH, '//p[@class="caption"]').text
            url = check.get_attribute("src")
            print(img_desc)
            additional_images(img_desc)
            browser.quit()
            time.sleep(2)
            file = open(os.path.dirname(__file__) + "\\Data\\" + "%s.txt" % (date), "w")
            file.write(title + "\n" +link )
            pic_name = os.path.dirname(__file__) + "\\Data\\" + date + "_0.png"
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

browser.implicitly_wait(5)
my_preference = open(os.path.dirname(__file__)+"//my_news_link.txt","r+")
my_news = open(os.path.dirname(__file__)+"//my_full_news.txt","r+")
my_news_data = my_news.readlines()
sugg = my_preference.readlines()

if len(my_news_data) == 2:
    l = os.listdir(os.path.dirname(__file__) + "\\Data")
    for i in l:
        # All files in Data Folder is deleted
        os.remove(os.path.dirname(__file__) + "\\Data\\" + i)
        browser.implicitly_wait(5)
    print("No Scraping")
    time.sleep(2)
    with open(os.path.dirname(__file__) + "\\Data\\"+date+'.txt','w') as f:
        f.writelines(my_news_data)
    additional_images(my_news_data[0],1)
    my_news.truncate(0)
    browser.quit()
elif sugg != []:
    l = os.listdir(os.path.dirname(__file__) + "\\Data")
    for i in l:
        # All files in Data Folder is deleted
        os.remove(os.path.dirname(__file__) + "\\Data\\" + i)
        browser.implicitly_wait(5)
    print("selected scrap")
    select_scrap()
else:
    l = os.listdir(os.path.dirname(__file__) + "\\Data")
    for i in l:
        # All files in Data Folder is deleted
        os.remove(os.path.dirname(__file__) + "\\Data\\" + i)
        browser.implicitly_wait(5)
    print("auto scrape")
    auto_scrape()