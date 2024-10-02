import config
from random import choice
import telebot

API_TOKEN = '7517003067:AAFIa9vD3Skzl0ZgOxfvZzqLnESjgrKzulY'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=['joke'])
def joke_handler(message):
    joke = choice(["От любви до ненависти одно проигонорированное сообщение.", 
                   "Охота - это спорт, оссобенно когда патроны закончились, а кабан ещё жив...", 
                   "- Ты сейчас на удалёнке?; - Хуже, я на увольнёнке!", 
                   "Внучка, потерявшая летом на грядках у деда акварельные краски, всю зиму ела цветную капусту."])
    bot.reply_to(message, joke)


bot.infinity_polling()