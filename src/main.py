import os
import telebot
import threading
import time
import textwrap
from hunters.pararius import Pararius
from history import History

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
bot = telebot.TeleBot(BOT_TOKEN)

chat_ids = CHAT_ID.split(',')
print(f'Messages will be sent to: {chat_ids}')

@bot.message_handler(commands=['chatid'])
def send_chatid(message):
    bot.reply_to(message, f'Your Chat ID is {message.chat.id}')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'I\'m hunting some apartments right now!')

def send_message(message):
    for chat_id in chat_ids:
        bot.send_message(chat_id, message)

runHunters = True
def hunters():
    pararius = Pararius()

    print('Start hunters')
    pararius.start()
    history = History('history.txt')
    while runHunters:
        preys = []
        # Get preys
        try:
            preys += pararius.check()
        except Exception as e:
            print(f'Found error when running hunters: {str(e)}')

        # Filter preys
        filtered_preys = history.filter(preys)
        if len(filtered_preys) > 0:
            print(f'Found {len(filtered_preys)} new preys')

        # Send telegram message
        for prey in filtered_preys:
            message = textwrap.dedent(f'''
                Name: {prey.name}
                Agency: {prey.agency}
                Price: {prey.price}
                Link: {prey.link}
            ''')
            send_message(message)
        time.sleep(5*60)
    print('Stop hunters')
    pararius.stop()

t = threading.Thread(target=hunters)
t.start()
bot.infinity_polling()
runHunters = False
t.join()
