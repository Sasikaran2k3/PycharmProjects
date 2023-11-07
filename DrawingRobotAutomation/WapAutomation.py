import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def BeginWap():
    global browser1
    options = Options()
    options.add_argument(r'--user-data-dir=E:\UpgradeBuddy')
    service = Service(r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
    browser1 = webdriver.Chrome(service=service,options=options)

def WapTransfer(person):
    browser1.minimize_window()
    browser1.maximize_window()
    browser1.get("https://web.whatsapp.com/")
    # Finding the contact .... Since the browser1 is dynamic wait function is required
    browser1.implicitly_wait(120)
    print("Wap Opened")
    browser1.find_element(By.CSS_SELECTOR, 'div[role="textbox"]').send_keys(person, "\n")
    time.sleep(5)
    print("Typed the name")
def LastMsg():
    LastMsg=browser1.find_element(By.CSS_SELECTOR,'span[class="_11JPr selectable-text copyable-text"]')
    return(LastMsg.text)
    browser1.minimize_window()

def SendWap(Query):
    MsgBox = browser1.find_element(By.CSS_SELECTOR , 'div[title="Type a message"]')
    MsgBox.send_keys(Query)
    MsgBox.send_keys("\n")
    browser1.minimize_window()

def Close():
    input("Press Enter key to close")
    browser1.close()
