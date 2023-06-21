from collections import defaultdict

eating_diary = defaultdict(dict)
emotions_diary = defaultdict(dict)

class BedCommand(Exception):
    pass


def add_eating(message, eating_diary):
    split_message = message.text.split(maxsplit=5)
    _, date, meal, *rest = split_message
    eating_diary[date][meal] = rest

def add_emotions(message, emotions_diary):
    _, date, meal, *rest = message.text.split(maxsplit=3)
    emotions_diary[date][meal] = rest

def show_eat(message, eating_diary):
    split_message = message.split()
    result = []
    if split_message[1] in eating_diary:
        for meal, info in eating_diary[split_message[1]].items():
            result.append(f'{meal} - {info[-1]}')
            result.append(f'чувство голода до приема пищи - {info[0]}')
            result.append(f'чувство голода после приема пищи - {info[1]}')
            result.append('')
        return '\n'.join(result)
    else:
        raise BedCommand

def show_emotions(message, emotions_diary):
    split_message = message.split()
    result = []
    if split_message[1] in emotions_diary:
        for meal, info in emotions_diary[split_message[1]].items():
            result.append(f'{meal} - {info[-1]}')
        return '\n'.join(result)
    else:
        raise BedCommand



def del_eating(message, eating_diary):
    split_message = message.text.split()
    if len(split_message) == 2:
        del eating_diary[split_message[1]]
    elif len(split_message) > 2:
        del eating_diary[split_message[1]][split_message[2]]
    else:
        raise BedCommand

def del_emotions(message, emotions_diary):
    split_message = message.text.split()
    if len(split_message) == 2:
        del emotions_diary[split_message[1]]
    elif len(split_message) > 2:
        del emotions_diary[split_message[1]][split_message[2]]
    else:
        raise BedCommand
