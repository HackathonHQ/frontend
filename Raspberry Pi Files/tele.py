from keys import telebotkey
print(telebotkey)
import time, datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

now = datetime.datetime.now()
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    if command == '/hi':
        telegram_bot.sendMessage (chat_id, str("Hi! Aryan"))
    elif command == '/time':
        telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
    elif command == '/logo':
        telegram_bot.sendPhoto (chat_id, photo = "https://i.pinimg.com/avatars/circuitdigest_1464122100_280.jpg")
    elif command == '/yellow':
        GPIO.output(3,1)
    elif command == '/green':
        GPIO.output(5,1)
    elif command == '/red':
        GPIO.output(7,1)
    elif command == '/disco':    
        GPIO.output(13,1)
    elif command == '/all off':
        GPIO.output(3,0)
        GPIO.output(5,0)
        GPIO.output(7,0)
        GPIO.output(13,0)
        
telegram_bot = telepot.Bot(telebotkey)
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')
while 1:
    time.sleep(10)
