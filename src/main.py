import os
import telebot
import threading
import time
import textwrap
from hunters.pararius import Pararius
from hunters.kamernet import Kamernet
from hunters.gruno import Gruno
from hunters.wonen123 import Wonen123
from history import History

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
bot = telebot.TeleBot(BOT_TOKEN)

if CHAT_ID is not None:
    chat_ids = CHAT_ID.split(',')
else:
    chat_ids = []
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
        #print(message)

runHunters = True
def run_hunters():
    hunters =  [Wonen123(), Gruno(), Kamernet(), Pararius()]

    print('Start hunters')
    for hunter in hunters:
        hunter.start()
    history = History('history.txt')
    while runHunters:
        preys = []
        # Get preys
        for hunter in hunters:
            try:
                preys += hunter.hunt()
            except Exception as e:
                message = f'Found error when running hunter: {str(e)}'
                print(message)
                send_message(message)

        # Filter preys
        filtered_preys = history.filter(preys)
        if len(filtered_preys) > 0:
            print(f'Found {len(filtered_preys)} new preys')

        # Send telegram message
        for prey in filtered_preys:
            message = textwrap.dedent(f'''
                Name: {prey.name}
                {'Agency: ' + prey.agency if prey.agency is not None else ''}
                Price: {prey.price}
                Link: {prey.link}
            ''')
            send_message(message)
        time.sleep(5*60)
    print('Stop hunters')
    for hunter in hunters:
        hunter.stop()

t = threading.Thread(target=run_hunters)
t.start()
bot.infinity_polling()
runHunters = False
t.join()
