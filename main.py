import telebot
import commands

'''
1) Поправить функцию удаления. Одновременно выводит команда не найдена и щапись удалена
2) Создать функции по добавлению эмоций 
3) Создать функцию по удалению эмоций 
4) Добавить функцию вывода в тг бот приемов пищи - done
5) Добавить функцию вывода в тг бот эмоций 
6) Добавить информационую справку о интуитивном питании 
7) Добавить информационную справку о возможностях тг бота 
'''

TOKEN_API = '5958215581:AAGxUmz9lfKBWIsRymKArGI-b0WTvUkUdnw'

bot = telebot.TeleBot(TOKEN_API)

@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, 'Рада видеть вас в своем телеграм-боте!')

@bot.message_handler(commands=['add_meal'])
def help(message):
    commands.add_eating(message, commands.eating_diary)
    bot.send_message(message.chat.id, 'Команда добавлена')
    print(commands.eating_diary)

@bot.message_handler(commands=['del'])
def help(message):
    try:
        commands.del_eating(message, commands.eating_diary)
    except commands.BedDeleteCommand:
        bot.send_message(message.chat.id, 'Неправильно введена команда')
    except KeyError:
        bot.send_message(message.chat.id, 'Неправильно введена дата или прием пищи')

    bot.send_message(message.chat.id, 'Запись удалена')
    print(commands.eating_diary)

@bot.message_handler(commands=['add_emotions'])
def help(message):
   bot.send_message(message.chat.id, 'Работает')

@bot.message_handler(commands=['show_eat'])
def help(message):
    formated_text = commands.show_eat(message.text, commands.eating_diary)
    bot.send_message(message.chat.id, formated_text)



#@bot.message_handler(content_types=['text'])
#def base(message):
    #bot.send_message(message.chat.id, 'Введите одну из доступных команд')

bot.polling(none_stop=True)