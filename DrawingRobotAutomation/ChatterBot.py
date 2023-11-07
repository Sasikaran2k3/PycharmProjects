from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import wikipedia

import WapAutomation


def StartChatterBot():
    # To avoid a error .... Doesn't matter if it doesn't exist
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)
    # Bot Name
    global Pikachu, Trainer
    Pikachu = ChatBot("Pikachu", storage_adapter="chatterbot.storage.SQLStorageAdapter")
    Trainer = ChatterBotCorpusTrainer(Pikachu)
def BotTrain(file="ManoConversation.yml"):
    Pikachu.storage.drop()
    Trainer.train(r"C:\Users\HP\PycharmProjects\DrawingRobotAutomation" + "\\"+file)  # , "chatterbot.corpus.english")
    f = open("ManoConversation.yml", "a")
def BotResponse(In):
    In = In.lower()
    if "draw" in In:
        Splitted = In.split("draw")
        Response = Pikachu.get_response("Draw")
        Content = Splitted[-1]
        return Content, "draw"
    elif "write" in In:
        Splitted = In.split("write")
        Response = Pikachu.get_response("Write")
        Content = Splitted[-1]
        return Content, "write"
    else:
        Response = Pikachu.get_response(In)
        return Response, "Chat"


StartChatterBot()
BotTrain()