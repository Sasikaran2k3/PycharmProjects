from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
from subprocess import call
from pyautogui import write
print("Importing Done !!")
pat=r'chrome.exe --user-data-dir="E:\Chatterbot\Selenium Browser" --remote-debugging-port=1234'
call(r"C:\WINDOWS\system32\cmd.exe")
write(pat)
options = Options()
options.add_experimental_option("debuggerAddress","localhost:1234")
services = Service(r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = webdriver.Chrome(service=services, options=options)
print("Browser Ready")
browser.get("https://web.whatsapp.com/")