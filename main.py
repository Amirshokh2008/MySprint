import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message, 'Привет! Я твой бот для подготовки к HSK.')


bot.infinity_polling()

