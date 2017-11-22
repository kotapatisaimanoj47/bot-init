from chatterbot.trainers import ListTrainer #method to import trainer
from sqlalchemy.types import TypeDecorator, Unicode
import os
from chatterbot import ChatBot #this imports the chatbot

bot = ChatBot('Test',
        Logic_adapters = [
            'chatterbot.logic.no_knowledge_adapter',
            'chatterbot.logic.multi_adapter.py',
            'chatterbot.logic.logic_adapter',
            'chatterbot.logic.best_match',
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter'],
        datbase=unicode('../database.db')) #creates a chat bot


bot.set_trainer(ListTrainer)

for _file in os.listdir('files'):
    chats = open('files/'+_file, 'r').readlines()
    bot.train(chats)
    print('please be more specific im a bot designed to answer ds in a short ans sweet manner . i know i am dumb bear with me will ya')

while True:
    request = raw_input('you: ')
    response = bot.get_response(request)
    print(response)
