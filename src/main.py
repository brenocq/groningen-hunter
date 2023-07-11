import os
import telebot
import threading
import time
from hunters.pararius import Pararius

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['chatid'])
def send_chatid(message):
    bot.reply_to(message, f"Your Chat ID is {message.chat.id}")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello!! Panqueca there?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
        bot.reply_to(message, message.text)

runHunters = True
def hunters():
    pararius = Pararius()

    print('Start hunters')
    pararius.start()
    while runHunters:
        bot.send_message(CHAT_ID, 'Check apartments')
        pararius.check()
        time.sleep(10)
    print('Stop hunters')
    pararius.stop()

t = threading.Thread(target=hunters)
t.start()
bot.infinity_polling()
runHunters = False
t.join()
