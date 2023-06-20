from collections import defaultdict

eating_diary = defaultdict(dict)

class BedDeleteCommand(Exception):
    pass


def add_eating(message, eating_diary):
    split_message = message.text.split(maxsplit=5)
    _, date, meal, *rest = split_message
    #if date in eating_diary:
    eating_diary[date][meal] = rest
    #else:
    #    eating_diary[date] = {meal:rest}


def del_eating(message, eating_diary):
    split_message = message.text.split()
    if len(split_message) == 2:
        del eating_diary[split_message[1]]
    elif len(split_message) > 2:
        del eating_diary[split_message[1]][split_message[2]]
    else:
        raise BedDeleteCommand


def show_eat(message, eating_diary):
    split_message = message.split()
    result = []
    for meal, info in eating_diary[split_message[1]].items():
        result.append(f'{meal} - {info[-1]}')
        result.append(f'чувство голода до приема пищи - {info[0]}')
        result.append(f'чувство голода после приема пищи - {info[1]}')
        result.append('')
    return '\n'.join(result)


'''
/add 11.10.2020 завтрак 1 3 огурец и кофе 
'''