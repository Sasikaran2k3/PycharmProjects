from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime

s = Service(r'C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe')
browser = webdriver.Chrome(service=s)
def Login(userId,password):
    UserId = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    UserId.send_keys(userId)
    Password = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    Password.send_keys(password)
    sbutton = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
    sbutton.click()
def InstaMessenger(userId='24_mano_09',password='mano2003@,',person='',content="This is an Automated Message !! NeverMind. :) "+str(datetime.datetime.now())+' is the time'):
    url='https://www.instagram.com'
    browser.get(url)
    browser.implicitly_wait(10)
    try:
        Login(userId,password)
    except:
        browser.refresh()
        Login(userId,password)
    browser.implicitly_wait(50)
    PassRemBut=browser.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')
    MessageBut=browser.find_element(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
    MessageBut.click()

    NotifBut=browser.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[3]/button[2]').click()
    browser.refresh()
    sendmes=browser.find_element(By.CSS_SELECTOR,"button[class='sqdOP  L3NKy   y3zKF     ']").click()

    for i in person:
        searchPeople=browser.find_element(By.XPATH,'/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
        selectButton=browser.find_element(By.CSS_SELECTOR,"button[class='wpO6b  ']").click()


    nxtButton=browser.find_element(By.CSS_SELECTOR,"button[class='sqdOP yWX7d    y3zKF   cB_4K  ']").click()

    MsgContent=browser.find_element(By.CSS_SELECTOR,'textarea[placeholder="Message..."]').send_keys(content,Keys.RETURN)
    try:
        ComeOut=browser.find_element(By.CSS_SELECTOR,"div[class='RnEpo  Yx5HN      ']").click()
    except:
            pass
    browser.implicitly_wait(5)


InstaMessenger(person=['a_nughty_gntle_grl08'])
browser.quit()