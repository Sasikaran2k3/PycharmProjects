import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def unReadMsg():
    unReadMsg = WebDriverWait(browser, 1000).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'div[class="_1pJ9J"]')))
    unReadMsg.click()
def lastMsg():
    time.sleep(5)
    try:
        LastMsg =browser.find_elements(By.CSS_SELECTOR, 'div[class="_1-FMR message-in focusable-list-item"]')[-1].text.split('\n')[0]
    except:
        print("LeftClick Error ... Maybe")
        browser.refresh()
    # This LastMsg returs 2 string seperated by \n so 1st line has actual data and 2nd line with timestamp
    myLastMsg = browser.find_elements(By.CSS_SELECTOR, 'div[class="_1-FMR message-out focusable-list-item"]')#[-1].text.split('\n')[0]
    if myLastMsg != []:
        myLastMsg = myLastMsg[-1].text.split('\n')[0]
    print(myLastMsg)
    return [LastMsg, myLastMsg]
def NumberThem(Lists):
    string = ""
    for i in range(len(Lists)):
        string+=str(i)+". "+Lists[i]
    return string+"D1\n"
def TextBoxWrite(data):
    TBox = browser.find_element(By.CSS_SELECTOR, 'p[class="selectable-text copyable-text"]')
    print(data)
    TBox.send_keys(data)
def ListDomain(content):
    file = open("DomainList.txt","r")
    content = file.readlines()
    print(content)
    numbered = NumberThem(content)
    print(numbered)
    TextBoxWrite(numbered)
def CloseChat():
    browser.find_element(By.CSS_SELECTOR,'div[data-tab="6"][title="Menu"]').click()
    browser.find_element(By.CSS_SELECTOR,'div[aria-label="Close chat"]').click()
def QueryProcessor(l):
    l[0] = int(l[0])
    if(l[1] == None):
        ListDomain(content)
    elif(l[1] == "D1"):
        if(l[0] >=0 and l[0]<=6):
            TextBoxWrite("You have selected ")
opt=Options()
#options.add_experimental_option("debuggerAddress","localhost:1234")
opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\Whatsapp')
#opt.add_argument("--headless")
services = Service(r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser=Chrome(service=services,options=opt)
browser.get("https://web.whatsapp.com/")
print("Opened")
browser.implicitly_wait(15)

while True:
    print("waiting")
    #try:
    unReadMsg()
    # All the unread Msg is cleared ... So create a Excel file and check for each contact
    query = lastMsg()
    QueryProcessor(query)
    CloseChat()
    file = open("DomainList.txt", "r")
    content = file.readlines()