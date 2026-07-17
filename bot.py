import os
import telebot

# Токен берется из настроек Fly.io
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Бот успешно запущен на сервере!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я получил твое сообщение: " + message.text)

if __name__ == '__main__':
    bot.infinity_polling()
