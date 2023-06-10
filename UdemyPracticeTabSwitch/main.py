import time
import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")

browser = Chrome(service=services)
browser.maximize_window()
browser.get("https://rahulshettyacademy.com/loginpagePractise/")
time.sleep(1)
browser.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

tabs = browser.window_handles

browser.switch_to.window(tabs[1])
time.sleep(2)
name = browser.find_element(By.XPATH,'//p[@class="im-para red"]/strong').text
assert name == "mentor@rahulshettyacademy.com"

browser.close()
browser.switch_to.window(tabs[0])
browser.find_element(By.CSS_SELECTOR, 'input#username').send_keys(name)
browser.find_element(By.CSS_SELECTOR, 'input#password').send_keys("learning")
browser.find_element(By.CSS_SELECTOR, 'input#terms').click()
browser.find_element(By.CSS_SELECTOR,'input#signInBtn').click()

wait = WebDriverWait(browser,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'.alert-danger strong')))
print(browser.find_element(By.CSS_SELECTOR,'.alert-danger strong'). text)
