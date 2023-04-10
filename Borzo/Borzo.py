
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
try:
    numbers = [9150581968,9566979881,6369029718]
    opt = Options()
    opt.add_argument(r"--user-data-dir=E:\Hackathon\BrowserChromes\WebScrap")
    service = Service(r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
    browser = Chrome(options=opt,service=service)
    f = open(r"E:\Hackathon\untitle_sih\ConsumerDetails.txt","r")
    content = f.read().split("\n")
    browser.get("https://borzodelivery.com/in")
    time.sleep(3)
    print(content)
    data = content[5]
    browser.implicitly_wait(10)
    a=browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Pick-up"]')
    a.send_keys(data)
    time.sleep(1)
    a.send_keys(Keys.ARROW_DOWN)
    a.send_keys(Keys.ENTER)
    a=browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Drop-off"]')
    a.send_keys(data)
    time.sleep(1)
    a.send_keys(Keys.ARROW_DOWN)
    a.send_keys(Keys.ENTER)
    browser.find_element(By.CSS_SELECTOR,'button[data-testid="unique-mini-form__submit-address"]').click()

    browser.find_element(By.CSS_SELECTOR, 'input[data-testid="unique-order-form__point-phone-0"]').send_keys(Keys.ARROW_LEFT*11)
    browser.find_element(By.CSS_SELECTOR, 'input[data-testid="unique-order-form__point-phone-0"]').send_keys(numbers[0])
    browser.find_element(By.CSS_SELECTOR, 'textarea[class="OrderTextarea_Root_3bG6h"]').send_keys(content[4])
    browser.find_element(By.CSS_SELECTOR, 'input[data-testid="unique-order-form__point-phone-1"]').send_keys(Keys.ARROW_LEFT*11)
    browser.find_element(By.CSS_SELECTOR, 'input[data-testid="unique-order-form__point-phone-1"]').send_keys(1212121212)
    browser.find_element(By.CSS_SELECTOR, 'textarea[data-testid="unique-order-form__point-note-1"]').send_keys("No4. Annanagar, Limekln st, Chennai")
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Parcel Value"]').send_keys(0)
    browser.find_element(By.CSS_SELECTOR, 'li[data-testid="unique-order-form__matter-variant-1"]').click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'button[data-testid="unique-order-form__create-button"]').click()
    #browser.find_element(By.CSS_SELECTOR, 'button[class="Button_Button_1tpBy Button_ButtonMedium_3seGY Button_Primary_2qt9c Button_Rect_3x530"]').click()
    #time.sleep(10)
    code = browser.find_element(By.CSS_SELECTOR, 'strong[class="color-decorative done-accepted-order-name"]').text

    browser.find_element(By.CSS_SELECTOR, 'body > div.layout > header > div > div > div.dv-header__menu > div.dv-header__desktop-menu > nav > div:nth-child(2) > a > span > button').click()
    browser.find_elements(By.CSS_SELECTOR, 'div[class="address-cell__tracking-url"]')[0].click()

    f = open("track.txt","w")
    f.write(code+"\n")
    f.close()
except:
    pass