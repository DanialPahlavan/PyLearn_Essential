import telebot
BotTokenIdAdr = ""

bot = telebot.TeleBot(BotTokenIdAdr) 



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bot started!")

@bot.message_handler(commands=['hello'])
def say_hello(message):
    bot.reply_to(message, "Hello World")




# continuously fetch new updates from telegram ...
bot.polling()
