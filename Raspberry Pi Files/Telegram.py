import time, datetime
import telepot
from telepot.loop import MessageLoop
from keys import telebotkey
print(telebotkey)

now = datetime.datetime.now()
def action (msg):
    chat_id = msg['chat'] ['id']
    command = msg['text']




if command == '/hi':
        telegram_bot.sendmesssage (chat_id, str("Hi Aryan"))


telegram_bot = telepot.bot(telebotkey)
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()


while 1:
    time.sleep(10)
    
