from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import wikipedia

def Start_Bot():
    log=logging.getLogger()
    log.setLevel(logging.CRITICAL)
    global BotObject
    BotObject = ChatBot("Pikachu",storage_adapter="chatterbot.storage.SQLStorageAdapter")
    BotTrainer=ChatterBotCorpusTrainer(BotObject)
    #BotTrainer.train(r"C:\Users\HP\PycharmProjects\MyChatterbot\MyConversation.yml","chatterbot.corpus.english")

def GetResponseFromBot(Question):
    Resp=BotObject.get_response(Question)
    return Resp

def OpenWhatsapp():
    s = Service(r'C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe')
    opt=Options()
    opt.add_experimental_option("debuggerAddress","localhost:1234")
    browser = webdriver.Chrome(service=s,options=opt)
    browser.get("https://web.whatsapp.com/")


#OpenWhatsapp()
Start_Bot()
while True:
    BotObject.storage.drop()
    Quest=input("\nMe: ")
    Response = GetResponseFromBot(Quest)
    print(Response)