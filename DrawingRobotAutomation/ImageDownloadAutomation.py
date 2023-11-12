import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import cv2

import InkScape
import WapAutomation


def BeginSelinium():
    global browser
    options = Options()
    #options.add_experimental_option("debuggerAddress","localhost:1234")
    services = Service(r"C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe")
    browser = webdriver.Chrome(service=services,options=options)

def Search(text="RMD Engieering College"):
    browser.get("https://www.google.com/imghp")
    browser.find_element(By.XPATH, "//textarea[@type='search']").click()
    browser.find_element(By.XPATH, "//textarea[@type='search']").send_keys(text + " outline\n")
    time.sleep(5)
    WapAutomation.BeginWap()
    WapAutomation.WapTransfer("DRAWING_ROBOT")
    WapAutomation.SendWap("Begining to Download")
    time.sleep(5)
    browser.minimize_window()
    index = int(input("Enter the position of Image in Web: "))
    List_Of_Img=browser.find_elements(By.CSS_SELECTOR,'img[class="rg_i Q4LuWd"]')
    Img=List_Of_Img[index-1]
    Img.screenshot("E:\\Collections of Gcode\\"+text+".png")
    print("Downloaded")
    Img=cv2.imread("E:\\Collections of Gcode\\"+text+".png")
    print("E:\\Collections of Gcode\\"+text+".png")
    cv2.imshow(text,Img)
    browser.minimize_window()
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    browser.close()
    return "E:\\Collections of Gcode\\"+text+".png"

#BeginSelinium()
path = r"E:\Collections of Gcode\pencil_sketch.jpg"
InkScape.BeginInk()
InkScape.StartDraw(path)
InkScape.Trace_BitImage()
InkScape.OpenExtention()