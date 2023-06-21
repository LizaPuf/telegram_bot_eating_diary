import telebot
import commands
import constants


TOKEN_API = '5958215581:AAGxUmz9lfKBWIsRymKArGI-b0WTvUkUdnw'
USER_ID = ''


bot = telebot.TeleBot(TOKEN_API)


@bot.message_handler(commands=['start'])
def main(message):
    username = message.from_user.username
    bot.send_message(message.chat.id, f'{username}, рада видеть вас в своем телеграм-боте!')
    bot.send_message(message.chat.id, constants.help)


@bot.message_handler(commands=['add_meal'])
def help(message):
    user_id = message.from_user.id
    try:
        commands.add_eating(user_id, message, commands.eating_diary)
        bot.send_message(message.chat.id, 'Команда добавлена')
        print(commands.eating_diary)
    except commands.BadCommand:
        bot.send_message(message.chat.id, 'Неправильно введена команда')


@bot.message_handler(commands=['add_emotions'])
def help(message):
    user_id = message.from_user.id
    try:
        commands.add_emotions(user_id, message, commands.emotions_diary)
        bot.send_message(message.chat.id, 'Команда добавлена')
        print(commands.emotions_diary)
    except commands.BadCommand:
        bot.send_message(message.chat.id, 'Неправильно введена команда')


@bot.message_handler(commands=['show_eat'])
def help(message):
    user_id = message.from_user.id
    try:
        formated_text = commands.show_eat(user_id, message.text, commands.eating_diary)
        bot.send_message(message.chat.id, formated_text)
    except commands.BadCommand:
        bot.send_message(message.chat.id, 'Неправильно введена команда')
    except KeyError:
        bot.send_message(message.chat.id, 'Неправильно введена дата или прием пищи')


@bot.message_handler(commands=['show_emotions'])
def help(message):
    user_id = message.from_user.id
    try:
        formated_text = commands.show_emotions(user_id, message.text, commands.emotions_diary)
        bot.send_message(message.chat.id, formated_text)
    except commands.BadCommand:
        bot.send_message(message.chat.id, 'Неправильно введена команда')
    except KeyError:
        bot.send_message(message.chat.id, 'Неправильно введена дата или прием пищи')


@bot.message_handler(commands=['del_meal'])
def help(message):
    user_id = message.from_user.id
    try:
        commands.del_eating(user_id, message, commands.eating_diary)
    except commands.BadCommand:
        bot.send_message(message.chat.id, 'Неправильно введена команда')
    except KeyError:
        bot.send_message(message.chat.id, 'Неправильно введена дата или прием пищи')
    else:
        bot.send_message(message.chat.id, 'Запись удалена')
        print(commands.eating_diary)


@bot.message_handler(commands=['del_emotions'])
def help(message):
    user_id = message.from_user.id
    try:
        commands.del_emotions(user_id,message, commands.emotions_diary)
    except commands.BadCommand:
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