import time
import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
urls = ["https://www.thehindubusinessline.com/search/?q=Agriculture%20in%20India%20&start=10",]
options = Options()
#options.add_experimental_option("debuggerAddress","localhost:1234")
options.add_argument("--headless")
options.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\WebScrap')
services = Service(r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=options)
browser.maximize_window()
browser.get(urls[0])
browser.implicitly_wait(20)
total_height = int(browser.execute_script("return document.body.scrollHeight"))
f = open("Hackthon_2022/news.txt", "w")
for i in range(0,total_height,1):
    browser.execute_script("window.scrollTo(0, %d);"%i)
time.sleep(5)
imgs = browser.find_elements(By.CSS_SELECTOR,'div[class="col-sm-3 col-xs-4 col-md-3"] img[class="mblcommonimg"]')
news = browser.find_elements(By.CSS_SELECTOR,'h3[class="title marginBottom10"] a')
finalNews = []
link = []
count =0
for i in range(0,len(news)+1):
    if i%2!=0:
        finalNews.append(news[i].text)
        #print(news[i].text)
        link.append(news[i].get_attribute("href"))
        count+=1
    #print(imgs[i].get_attribute("src"))
print(len(finalNews),len(link),len(imgs))
for i in range(10):
    f.write(str(finalNews[i])+"\n"+str(link[i])+"\n"+str(imgs[i].get_attribute("src"))+"\n")
f.close()




