import telebot
import commands

TOKEN_API = '5958215581:AAGxUmz9lfKBWIsRymKArGI-b0WTvUkUdnw'

bot = telebot.TeleBot(TOKEN_API)

@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, 'Рада видеть вас в своем телеграм-боте!')

@bot.message_handler(commands=['add'])
def help(message):
    commands.add_eating(message, commands.eating_diary)
    bot.send_message(message.chat.id, 'Команда добавлена')
    print(commands.eating_diary)



#@bot.message_handler(content_types=['text'])
#def base(message):
    #bot.send_message(message.chat.id, 'Введите одну из доступных команд')

bot.polling(none_stop=True)