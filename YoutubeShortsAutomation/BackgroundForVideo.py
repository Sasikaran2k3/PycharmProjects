import time
import os
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def Initialize():
    opt = Options()
    # opt.add_experimental_option('debuggerAddress',"localhost:1135") #CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
    opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')
    services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
    global browser
    browser = Chrome(service=services, options=opt)
    browser.maximize_window()


def putOnEditor():
    browser.implicitly_wait(10)
    browser.get("https://www.kapwing.com/studio/editor/subtitles")
    browser.find_element(By.XPATH, '//input[@data-cy="upload-input"]').send_keys(os.getcwd() + "\\Data\\" + "1.mp4")
    wait = WebDriverWait(browser, 1000)
    wait.until(expected_conditions.invisibility_of_element(
        (By.XPATH, '//img[@src="/assets/pending-media-upload-icon.e21cbd1d.gif"]')))

    print("Video  Imported")
    browser.find_element(By.XPATH, '//div[@data-cy="resize-canvas-button"]').click()
    browser.find_element(By.XPATH, '//div[@data-cy="916-small-control-button"][1]').click()
    browser.find_element(By.XPATH, '//button[@data-cy="resize-apply"]').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//button[@class="MagicSubtitleStart-module_primaryButton_uyrZz"]').click()
    browser.find_element(By.XPATH, '//button[@class="MagicSubtitleTranscribe-module_startButton_BgFeR"]').click()
    wait.until(expected_conditions.presence_of_element_located(
        (By.XPATH, '(//div[@class="PresetPreview-module_preview_YpGeo"])[2]')))
    print("Selecting Style")
    time.sleep(2)
    browser.find_element(By.XPATH, '//div[@class="Track-module_container_mph21"][1]').click()
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, 'textarea[data-cy="magic-textarea"]').click()
    print("Changing Position")
    act = ActionChains(browser)
    transform = browser.find_elements(By.XPATH, '//div[@data-cy="drag-handler"]')
    act.click_and_hold(transform[1]).move_to_element_with_offset(transform[0], 90, 120)
    act.release().perform()
    parent = browser.find_elements(By.XPATH, '//div[@class="PresetPreview-module_container_034hO"]')
    for i in parent:
        if i.find_element(By.TAG_NAME, 'input').get_attribute("value") == "My":
            i.click()
            break
    browser.find_element(By.CSS_SELECTOR, 'div[data-cy="create-button"]').click()
    browser.find_element(By.CSS_SELECTOR, 'div[data-cy="export-panel-create-button"]').click()
    browser.find_element(By.CSS_SELECTOR,
                         'div[class = "common-module_smallControlButton_66vuT ExportRow-module_buttonStyle_L6WYa ExportRow-module_studioColor_ltubC "]').click()
    time.sleep(7)
    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//div[@class="VideoContainer-module_commentsMetaDataFileSize_E7zW4"]')))
    browser.find_element(By.XPATH,
                         '//div[@class="VideoContainer-module_topEditRight_tnjnu"]/button[@class = "VideoPageButton-module_actionButton_-OxGR"]').click()


def demo():
    browser.implicitly_wait(10)
    browser.find_element(By.CSS_SELECTOR, 'textarea[data-cy="magic-textarea"]').click()
    act = ActionChains(browser)
    transform = browser.find_elements(By.XPATH, '//div[@data-cy="drag-handler"]')
    act.click_and_hold(transform[1]).move_to_element_with_offset(transform[0], 90, 120)
    act.release().perform()
