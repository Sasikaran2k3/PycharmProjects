import time
import os
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


def Initialize():
    opt = Options()
    # This option is used to verify the action part without starting from beginning
    opt.add_experimental_option('debuggerAddress',"localhost:1135") #CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
    opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')
    services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
    global browser
    browser = Chrome(service=services, options=opt)
    browser.maximize_window()


def putOnEditor():
    browser.implicitly_wait(10)
    # Count finds no of times error happens and if count is more than 10, Program stops
    count = 0
    j = 0
    # Queue is list of tasks of 5 videos
    Queue = list(range(0, 5))
    while True:
        try:
            while Queue != []:
                browser.get("https://www.kapwing.com/studio/editor/subtitles")
                browser.find_element(By.XPATH, '//input[@data-cy="upload-input"]').send_keys(
                    os.getcwd() + "\\Data\\" + "%d.mp4" % j)
                wait = WebDriverWait(browser, 1000)
                # Wait till the upload symbol gets invisible
                wait.until(expected_conditions.invisibility_of_element(
                    (By.XPATH, '//img[@src="/assets/pending-media-upload-icon.e21cbd1d.gif"]')))

                print("Video  Imported")
                browser.find_element(By.XPATH, '//div[@data-cy="resize-canvas-button"]').click()
                browser.find_element(By.XPATH, '//div[@data-cy="916-small-control-button"][1]').click()
                browser.find_element(By.XPATH, '//button[@data-cy="resize-apply"]').click()
                time.sleep(2)
                browser.find_element(By.XPATH,
                                     '//button[@class="MagicSubtitleStart-module_primaryButton_uyrZz"]').click()
                browser.find_element(By.XPATH,
                                     '//button[@class="MagicSubtitleTranscribe-module_startButton_BgFeR"]').click()
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
                # moves the subtitle from the video bottom left position
                act.click_and_hold(transform[1]).move_to_element_with_offset(transform[0], 100, 120)
                act.release().perform()
                parent = browser.find_elements(By.XPATH, '//div[@class="PresetPreview-module_container_034hO"]')
                # selects the subtitle style
                for i in parent:
                    if i.find_element(By.TAG_NAME, 'input').get_attribute("value") == "My":
                        i.click()
                        break

                browser.find_element(By.CSS_SELECTOR, 'div[data-cy="create-button"]').click()
                browser.find_element(By.CSS_SELECTOR, 'div[data-cy="export-panel-create-button"]').click()
                browser.find_element(By.CSS_SELECTOR, 'div[class="KapwingInput-module_inputText_ECzwK"]>span').click()
                browser.find_element(By.CSS_SELECTOR, 'div[class ="ExportRow-module_inputWrapper_AV0p4"]>input').send_keys(Keys.CONTROL, "a", Keys.CONTROL, "%d\n" % j)
                #browser.find_element(By.CSS_SELECTOR, 'div[data-cy="create-button"]').click()
                #browser.find_element(By.CSS_SELECTOR, 'div[data-cy="export-panel-create-button"]').click()
                #browser.find_element(By.CSS_SELECTOR, 'span[class="KapwingInput-module_text_ly3QW"]').click()
                browser.find_element(By.CSS_SELECTOR,
                                     'div[class = "common-module_smallControlButton_66vuT ExportRow-module_buttonStyle_L6WYa ExportRow-module_studioColor_ltubC "]').click()
                time.sleep(7)
                print("Download Page")
                # Waits till the size of the file appears and then dowload button is clicked
                wait.until(expected_conditions.visibility_of_element_located(
                    (By.XPATH, '//div[@class="VideoContainer-module_commentsMetaDataFileSize_E7zW4"]')))
                browser.find_element(By.XPATH,
                                     '//div[@class="VideoContainer-module_topEditRight_tnjnu"]/button[@class = "VideoPageButton-module_actionButton_-OxGR"]').click()
                j += 1
                Queue.pop(0)
                print(Queue)
        except Exception as e:
            count += 1
            print("Error Encountered")
            print("Error Count : %d" % count)
            print(e)
            browser.refresh()
            if count > 10:
                break
        else:
            break
    time.sleep(50)
    print("Completed Successfully")
    browser.close()


def demo():
    """
    browser.find_element(By.CSS_SELECTOR, 'textarea[data-cy="magic-textarea"]').click()
    act = ActionChains(browser)
    transform = browser.find_elements(By.XPATH, '//div[@data-cy="drag-handler"]')
    act.click_and_hold(transform[1]).move_to_element_with_offset(transform[0], 100, 120)
    act.release().perform()
"""
    browser.implicitly_wait(10)
    browser.find_element(By.CSS_SELECTOR, 'div[data-cy="create-button"]').click()
    browser.find_element(By.CSS_SELECTOR, 'div[data-cy="export-panel-create-button"]').click()
    browser.find_element(By.CSS_SELECTOR, 'div[class="KapwingInput-module_inputText_ECzwK"]>span').click()
    browser.find_element(By.CSS_SELECTOR, 'div[class ="ExportRow-module_inputWrapper_AV0p4"]>input').send_keys(Keys.CONTROL, "a",Keys.CONTROL,"%d\n" % 0)

Initialize()
putOnEditor()