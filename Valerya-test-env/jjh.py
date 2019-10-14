import os
import telebot


TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Hi':
        bot.send_message(message.chat.id, 'Hello')
    else:
        atext = message.text[:3] + message.text.lower()
        bot.send_message(message.chat.id, atext)

bot.polling()