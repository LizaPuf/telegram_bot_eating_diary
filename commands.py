eating_diary = {}


def add_eating(message, eating_diary):
    split_message = message.text.split(maxsplit=6)
    if split_message[1] in eating_diary:
        eating_diary[split_message[1]][split_message[2]] = split_message[3:]
    else:
        eating_diary[split_message[1]] = {split_message[2]:split_message[3:]}



'''
/add 11.10.2020 завтрак 1 3 огурец и кофе 
'''