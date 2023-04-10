from gtts import gTTS
import wget
import os
from moviepy.editor import *
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

mode = 0o666


def Initialize():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
    global browser
    browser = Chrome(service=services)
    l = os.listdir(os.path.dirname(__file__)+"\\Data")
    for i in l:
        os.remove(os.path.dirname(__file__)+"\\Data\\"+i)
    browser.implicitly_wait(5)


def StartScarpingNews():
    f = open(os.path.dirname(__file__) + "\\Data\\newsFile.txt", "w")
    browser.get("https://www.gadgets360.com/news")

    print("Waiting to load... ")

    list_of_news = browser.find_elements(By.CSS_SELECTOR, 'span[class="news_listing"]')
    list_of_link = browser.find_elements(By.CSS_SELECTOR, 'div[class="thumb"]>a')

    if len(list_of_link) == len(list_of_news):
        for i in range(len(list_of_news)):
            f.write(list_of_news[i].text + " :: " + list_of_link[i].get_attribute("href") + "\n")
    else:
        f.write("Scrap Data Corrupted")
    f.close()


def StartScrapImage():
    f = open(os.path.dirname(__file__) + "\\Data\\newsFile.txt", "r")
    data = f.readlines()
    c = 0
    text = "div[class='fullstoryImage']>div[class = 'heroimg']>img"
    for i in data:
        title, link = i.split(" :: ")
        browser.get(link)
        print(text)
        try:
            check = browser.find_element(By.CSS_SELECTOR, text)
            url = check.get_attribute("src")
        except:
            print("img Not found")
            continue
        picName = os.path.dirname(__file__) + "\\Data\\" + str(c) + ".png"
        wget.download(url, out=picName)
        c += 1
    # Image Processing Example
    """
    url = "https://i.gadgets360cdn.com/large/whatsapp_outage_india_it_ministry_1666798329743.jpg?downsize=950:*"
    print(os.path.dirname(__file__))
    os.chdir(os.path.dirname(__file__)+"\\Data")
    wget.download(url,out="1.png")
    """


def TurnOnTheSound():
    f = open(os.path.dirname(__file__) + "\\Data\\" + "newsFile.txt", "r")
    news = f.readlines()
    for i in range(len(news)):
        breakNews = news[i].split(" :: ")[0]
        obj = gTTS(text=breakNews, lang="en", slow=False)
        path = os.path.dirname(__file__) + "\\Data\\%i.mp3" % i
        obj.save(path)


def EditProcess():
    f = open(os.path.dirname(__file__) + "\\Data\\" + "newsFile.txt", "r")
    final = []
    news = f.readlines()
    for i in range(len(news)):
        audio = AudioFileClip(os.path.dirname(__file__)+"\\Data\\%d.mp3"%i)
        image = ImageClip(os.path.dirname(__file__)+"\\Data\\%d.png"%i)
        video = image.set_audio(audio)
        video.duration = audio.duration+1
        video.fps = 1
        video.write_videofile(os.path.dirname(__file__)+"\\Data\\%d.mp4"%i)
        final.append(video)
    end = concatenate_videoclips(final, method="compose")
    end.write_videofile(os.path.dirname(__file__)+"\\Data\\"+"Top20News.mp4")
    browser.quit()

