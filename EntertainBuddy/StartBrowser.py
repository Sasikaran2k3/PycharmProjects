import os

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def Start_Lap(browser_name="UpgradeBuddy"):
    # Initialization of web Driver
    opt = Options()
    # This option is used to verify the action part without starting from beginning
    # opt.add_experimental_option('debuggerAddress',"localhost:1135")
    # CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\Youtube\UpgradeBuddy"
    path_of_browser = os.path.dirname(__file__) + '\%s' % browser_name
    opt.add_argument(r'--user-data-dir=%s'%path_of_browser)
    services = Service(executable_path=os.path.dirname(__file__) + "\chromedriver.exe")
    browser = Chrome(service=services, options=opt)
    browser.maximize_window()
    browser.implicitly_wait(15)
    return browser


def Start_Pc(browser_name="UpgradeBuddy"):
    opt = Options()
    # This option is used to verify the action part without starting from beginning
    # opt.add_experimental_option('debuggerAddress', "localhost:1135")
    # CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Youtube\UpgradeBuddy"
    opt.add_argument(r'--user-data-dir=E:\Youtube\%s' % browser_name)

    services = Service(executable_path=os.path.dirname(__file__) + "\chromedriver.exe")
    browser = Chrome(service=services, options=opt)
    browser.implicitly_wait(10)
    return browser