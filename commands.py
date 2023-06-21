from collections import defaultdict


eating_diary = defaultdict(lambda: defaultdict(dict))
emotions_diary = defaultdict(lambda: defaultdict(dict))


class BadCommand(Exception):
    pass


def add_eating(user_id, message, eating_diary):
    split_message = message.text.split(maxsplit=5)
    if len(split_message) == 1:
        raise BadCommand
    _, date, meal, *rest = split_message
    #if user_id in eating_diary:
    #     if date in eating_diary[user_id]:
    #         eating_diary[user_id][date][meal] = rest
    #     else:
    #         var_dict = {date:{meal : meal}}
    #         eating_diary[user_id] = var_dict
    #
    # else:
    #     eating_diary[user_id] = {date : {meal : rest}}
    eating_diary[user_id][date][meal] = rest


def add_emotions(user_id, message, emotions_diary):
    split_message = message.text.split(maxsplit=3)
    if len(split_message) == 1:
         raise BadCommand
    _, date, meal, *rest = split_message
    # if user_id in emotions_diary:
    #     emotions_diary[user_id][date][meal] = rest
    # else:
    #     emotions_diary[user_id] = {date : {meal : rest}}
    emotions_diary[user_id][date][meal] = rest


def show_eat(user_id,message, eating_diary):
    split_message = message.split()
    result = []
    user_eating_diary = eating_diary[user_id]
    if len(split_message) == 1:
        raise BadCommand
    if split_message[1] in user_eating_diary:
        for meal, info in user_eating_diary[split_message[1]].items():
            result.append(f'{meal} - {info[-1]}')
            result.append(f'чувство голода до приема пищи - {info[0]}')
            result.append(f'чувство голода после приема пищи - {info[1]}')
            result.append('')
        return '\n'.join(result)
        return '\n'.join(result)
    else:
        raise KeyError


def show_emotions(user_id, message, emotions_diary):
    split_message = message.split()
    result = []
    user_emotions_diary = emotions_diary[user_id]
    if len(split_message) == 1:
        raise BadCommand
    if split_message[1] in user_emotions_diary:
        for meal, info in user_emotions_diary[split_message[1]].items():
            result.append(f'{meal} - {info[-1]}')
        return '\n'.join(result)
    else:
        raise KeyError



def del_eating(user_id, message, eating_diary):
    split_message = message.text.split()
    user_eating_diary = eating_diary[user_id]
    if len(split_message) == 2:
        del user_eating_diary[split_message[1]]
    elif len(split_message) > 2:
        del user_eating_diary [split_message[1]][split_message[2]]
    elif len(split_message) == 1:
        raise BadCommand


def del_emotions(user_id,message, emotions_diary):
    split_message = message.text.split()
    user_emotions_diary = emotions_diary[user_id]
    if len(split_message) == 2:
        del user_emotions_diary[split_message[1]]
    elif len(split_message) > 2:
        del user_emotions_diary[split_message[1]][split_message[2]]
    else:
        raise BadCommand
