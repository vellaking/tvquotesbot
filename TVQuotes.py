# -*- coding: utf-8 -*-
import telebot, json, random

bot = telebot.TeleBot("172065140:AAFCKlHG1eVh0blJ8TdkUsia-2SfL1oRnHk")
welcomeMessage = ["Bolo boss..","Hukum mere aaka","Abe kya hai? subah subah joke chahie tereko?"]
helpMessage = ["Are, bas joke mangne ka", "I am a joke bot, there is not much to explain here.","This I do: Make jokes; what I don't do: Do dishes and about everything else.","I don't know what to say. /joke"]

buffyQuotes= []
with open('buffy.json', mode='r', encoding='utf8') as file:
    buffyQuotes = json.loads(file.read())

shieldQuotes= []
with open('shield.json', mode='r', encoding='utf8') as file:
    shieldQuotes = json.loads(file.read())
    
ddQuotes = []
with open('dd.json', mode='r', encoding='utf8') as file:
    ddQuotes = json.loads(file.read())
    
mrrobotQuotes= []
with open('mrrobot.json', mode='r', encoding='utf8') as file:
    mrrobotQuotes = json.loads(file.read())
    
tdQuotes= []
with open('truedetective.json', mode='r', encoding='utf8') as file:
    tdQuotes = json.loads(file.read())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, random.choice(welcomeMessage))

@bot.message_handler(commands=['help'])
def send_helpMsg(message):
    bot.reply_to(message, random.choice(helpMessage))

@bot.message_handler(commands=['buffy'])
def send_joke(message):
    bot.reply_to(message, random.choice(buffyQuotes))

@bot.message_handler(commands=['shield'])
def send_joke(message):
    bot.reply_to(message, random.choice(shieldQuotes))
    
@bot.message_handler(commands=['daredevil'])
def send_joke(message):
    bot.reply_to(message, random.choice(ddQuotes))

@bot.message_handler(commands=['mrrobot'])
def send_joke(message):
    bot.reply_to(message, random.choice(mrrobotQuotes))

@bot.message_handler(commands=['truedetective'])
def send_joke(message):
    bot.reply_to(message, random.choice(tdQuotes))

@bot.message_handler(commands=['stop'])
def send_joke(message):
    bot.reply_to(message, "Good night :)")
    bot.stoppolling()

bot.polling(interval=5)

##start - starts, duh
##help - well?
##buffy - Buffy the Vampire Slayer quotes
##shield - Agents of S.H.I.E.L.D. quotes
##daredevil - Marvel's Daredevil quotes
##mrrobot - Mr Robot quotes
##truedetective - True Detective quotes
##stop - idk what this does
