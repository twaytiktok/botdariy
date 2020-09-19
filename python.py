import telebot
import random
 
from telebot import types
 
bot = telebot.TeleBot("1106030218:AAGYMejJw_ujNXaKQU_qaStT1IUSPnvZdVE")

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            bot.send_message(chatid, text)


bot.set_update_listener(listener) #register listener
bot.polling()
#Use none_stop flag let polling will not stop when get new message occur error.
bot.polling(none_stop=True)
# Interval setup. Sleep 3 secs between request new message.
bot.polling(interval=3)

while True: # Don't let the main Thread end.
    pass

# RUN
bot.polling(none_stop=True)