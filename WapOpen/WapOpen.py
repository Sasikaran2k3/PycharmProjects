import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import pyautogui

os.startfile('cmd.exe')
time.sleep(1)
command='chrome.exe --user-data-dir="E:\Chatterbot\Selenium Browser" --remote-debugging-port=1234'
pyautogui.write(command+"\n")

options = Options()
options.add_experimental_option("debuggerAddress","localhost:1234")
services = Service(r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = webdriver.Chrome(service=services, options=options)

browser.get("https://web.whatsapp.com/")