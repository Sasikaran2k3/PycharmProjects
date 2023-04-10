# ChatterBot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import wikipedia

def Automate(question):
    s = Service(r'C:\Users\HP\PycharmProjects\WebDriver\chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    link = "https://www.google.com/"
    browser.minimize_window()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "input[class='gLFyf gsfi']").send_keys(question+"\n")
    Net_Answer=browser.find_element(By.CSS_SELECTOR, "div[class='O5uR6d LTKOO']").text
    return Net_Answer

def BotInteraction():
    # To avoid a error .... Doesn't matter if it doesn't exist
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)
    # Bot Name
    Pikachu=ChatBot("Pikachu",storage_adapter="chatterbot.storage.SQLStorageAdapter")
    Trainer=ChatterBotCorpusTrainer(Pikachu)
    # Here starts the training
    # Once Trained .... No need to train again

    Pikachu.storage.drop()
    Trainer.train(r"C:\Users\HP\PycharmProjects\MyChatterbot\ManoConversation.yml")#, "chatterbot.corpus.english")
    #Trainer.train("chatterbot.corpus.english")
    # Collect Questions/Conversation in a new YML file
    f = open("MyConversation.yml", "a")

    while(True):
        question=input("Question:")#question=UserQuestion
        if(question.lower()=="exit"):
            break
        elif(question.lower()=="reset my data"):
            # To clear datas Learned by Bot .... Change in data file Happens only if old data is removed
            Pikachu.storage.drop()
            print("All my memory is gone !!")
            continue
        # get_response is the function where u interact
        res=Pikachu.get_response(question)
        #f.write("\n # - - "+ question)
        f.write("\n- - "+question+" #")
        f.flush()
        if(res=="Sorry. I didn't get you... Can u give me answer for that ?"):
            ans=input("Can u answer that question:")
            if(ans.lower()=="yes"):
                Qans=input("Answer:")
                f.write("\n  - "+Qans)
                f.flush()
                print("Noted ... Thanks for information")
            else:
                try:
                    if ("what" in question.lower()):
                        print("Surfing...")
                        WQuestion=question.lower().replace("what is ","").replace("?","")
                        WebResult=wikipedia.summary(WQuestion, 1)
                        f.write("\n  - " + WebResult)
                        print(WebResult)
                except:
                    print("Web Surfing Error")
        else:
            print(res)
BotInteraction()