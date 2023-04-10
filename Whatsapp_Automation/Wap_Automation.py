from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("debuggerAddress","localhost:1234")
service = Service(r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = webdriver.Chrome(service=service,options=options)

# Check For new messages

def CheckForNewMsg():
    try:
        browser.find_element(By.CSS_SELECTOR,'span[class="l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt"]').click()
        print("Yes U Have New Message")
        try:
            browser.find_element(By.CSS_SELECTOR,'span[class="l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt"').click()
        except:
            print("some dynamic error")
            CheckForNewMsg()
    except:
        print("No New Msg")

def WapTransfer(person, content):
    browser.get("https://web.whatsapp.com/")

# Finding the contact .... Since the browser is dynamic wait function is required

    browser.implicitly_wait(120)
    print("Wap Opened")


    browser.find_element(By.CSS_SELECTOR,'div[role="textbox"]').send_keys(person,"\n")
    print("Typed the name")
# To FInd the Last Converstion therefore ChatterBot Starts Interaction
def LastMsg():
    LastMsg=browser.find_element(By.CSS_SELECTOR,'span[class="i0jNr selectable-text copyable-text"]')
    return(LastMsg.text)



def Close():
    input("Press Enter key to close")
    browser.close()

