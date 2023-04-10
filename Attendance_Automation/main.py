import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
    driver = Service(r'C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe')
web = webdriver.Chrome(service=driver)
def GoogleLogin(Userid="21102133@rmd.ac.in",password="sasi@rmd"):
    web.get('https://mail.google.com/mail/u/0/#inbox')
    UserId = web.find_element(By.CSS_SELECTOR, 'input[type="email"]')
    UserId.send_keys(Userid)
    web.find_element(By.CSS_SELECTOR, "button[class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b']").click()
    web.implicitly_wait(40)
    time.sleep(2)
    web.find_element(By.CSS_SELECTOR, 'input[type="email"]')
    web.find_element(By.CSS_SELECTOR, "button[class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b']").click()

GoogleLogin()
FormLink=input("Link: ")
web.get(FormLink)
