import telebot
import commands
import constants


TOKEN_API = '5958215581:AAGxUmz9lfKBWIsRymKArGI-b0WTvUkUdnw'

bot = telebot.TeleBot(TOKEN_API)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Рада видеть вас в своем телеграм-боте!')
    bot.send_message(message.chat.id, constants.help)

@bot.message_handler(commands=['add_meal'])
def help(message):
    commands.add_eating(message, commands.eating_diary)
    bot.send_message(message.chat.id, 'Команда добавлена')
    print(commands.eating_diary)


@bot.message_handler(commands=['add_emotions'])
def help(message):
    commands.add_emotions(message, commands.emotions_diary)
    bot.send_message(message.chat.id, 'Команда добавлена')
    print(commands.emotions_diary)

@bot.message_handler(commands=['show_eat'])
def help(message):
    try:
        formated_text = commands.show_eat(message.text, commands.eating_diary)
        bot.send_message(message.chat.id, formated_text)
    except commands.BedCommand:
        bot.send_message(message.chat.id, 'Неправильно введена команда')
    except KeyError:
        bot.send_message(message.chat.id, 'Неправильно введена дата или прием пищи')

@bot.message_handler(commands=['show_emotions'])
def help(message):
    try:
        formated_text = commands.show_emotions(message.text, commands.emotions_diary)
        bot.send_message(message.chat.id, formated_text)
    except commands.BedCommand:
        bot.send_message(message.chat.id, 'Неправильно введена команда')
    except KeyError:
        bot.send_message(message.chat.id, 'Неправильно введена дата или прием пищи')


@bot.message_handler(commands=['del_eat'])
def help(message):
    try:
        commands.del_eating(message, commands.eating_diary)
    except commands.BedCommand:
        bot.send_message(message.chat.id, 'Неправильно введена команда')
    except KeyError:
        bot.send_message(message.chat.id, 'Неправильно введена дата или прием пищи')
    else:
        bot.send_message(message.chat.id, 'Запись удалена')
        print(commands.eating_diary)

@bot.message_handler(commands=['del_emotions'])
def help(message):
    try:
        commands.del_emotions(message, commands.emotions_diary)
    except commands.BedCommand:
        bot.send_message(message.chat.id, 'Неправильно введена команда')
    except KeyError:
        bot.send_message(message.chat.id, 'Неправильно введена дата или прием пищи')
    else:
        bot.send_message(message.chat.id, 'Запись удалена')
        print(commands.eating_diary)



@bot.message_handler(commands=['INFO'])
def help(message):
    img = open('img1.png', 'rb')

    bot.send_photo(message.chat.id, img, caption=constants.eating_info)


bot.polling(none_stop=True)