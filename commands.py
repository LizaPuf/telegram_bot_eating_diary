from collections import defaultdict

eating_diary = defaultdict(dict)


def add_eating(message, eating_diary):
    split_message = message.text.split(maxsplit=6)
    _, date, meal, *rest = split_message
    #if date in eating_diary:
    eating_diary[date][meal] = rest
    #else:
    #    eating_diary[date] = {meal:rest}


def del_eating(message, eating_diary):
    split_message = message.text.split()



'''
/add 11.10.2020 завтрак 1 3 огурец и кофе 
'''