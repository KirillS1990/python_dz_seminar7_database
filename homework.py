import re


def add_work():
    with open("homework.txt", "a") as file:
        text = input('Напишите предмет и домашнее задание к нему:')
        file.writelines(text)
    


def delete():
    with open('homework.txt') as f:
        lines = f.readlines()

    str = input('Напишите предмет по которому удалить домашнее задание:')
    pattern = re.compile(re.escape(str))
    with open('homework.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)