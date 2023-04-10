from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging


logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

Pikachu = ChatBot("Pikachu",storage_adapter="chatterbot.storage.SQLStorageAdapter")
Master=ChatterBotCorpusTrainer(Pikachu)
Master.train("chatterbot.corpus.data.custom)")

question=''
while(question.lower()!="exit"):
    question=input("Question:")
    response=Pikachu.get_response(question)
    print(response)
