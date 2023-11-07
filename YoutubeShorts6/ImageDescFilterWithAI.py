import os
import time
import nltk
import datetime
from nltk.tokenize import word_tokenize
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


date = "".join(str(datetime.date.today()).split("-"))
f = open(os.path.dirname(__file__)+"/Data/"+date+".txt",'r')
data = f.readlines()

# Sample news title
news_title =data[0].replace("\n", "")

# Tokenize the news title
words = word_tokenize(news_title)

# Perform POS tagging
tagged_words = nltk.pos_tag(words)

# Define the parts of speech tags for descriptive words
descriptive_tags = ['NN', 'NNS', 'NNP', 'NNPS', 'JJ']

# Filter out words with the specified parts of speech
filtered_words = [word for word, tag in tagged_words if tag in descriptive_tags]

# Display the filtered descriptive keywords
print(filtered_words)

# Initalization of web Driver
opt = Options()

# This option is used to verify the action part without starting from beginning
#opt.add_experimental_option('debuggerAddress',"localhost:1135")  # CMD prompt is chrome.exe --remote-debugging-port=1135 --user-data-dir="E:\Hackathon\BrowserChromes\AutomateEdit"
opt.add_argument(r'--user-data-dir=E:\Hackathon\BrowserChromes\AutomateEdit')

services = Service(executable_path=r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
browser = Chrome(service=services, options=opt)
browser.maximize_window()
browser.implicitly_wait(15)

for i in range(len(filtered_words)):
    browser.get("https://www.google.com/imghp")
    browser.find_element(By.XPATH, "//textarea[@type='search']").click()
    browser.find_element(By.XPATH, "//textarea[@type='search']").send_keys(filtered_words[i] + "\n")
    all_img = browser.find_elements(By.XPATH, '//div[@class="fR600b islir"]//img')[0]
    all_img.click()
    time.sleep(4)
    url = browser.find_elements(By.XPATH, '//div[@class="MAtCL PUxBg"]//img')
    pic_name = os.path.dirname(__file__) + "\\Data\\" + date + "_%d" % i + ".png"
    for j in url :
        if "http" in j.get_attribute("src"):
            j.screenshot(pic_name)
            print("downloaded")
            break
browser.quit()
