from viewer import view_homework as vh
from viewer import view_shedule as vs
from teacher import teach


def menu():
    while True:
        print('============================================')
        print('1 - Студент')
        print('2 - Преподаватель')
        print('3 - Выход')
        print('============================================')
        number = input('Выберете пункт меню: ')
        
        if number == '1':
            print('============================================')
            print('1. Посмотреть расписание')
            print('2. Посмотреть домашнее задание')
            print('============================================')
            num = input('Выберете пункт меню: ')
            if num == "1":
                print(vs())
            if num == '2':
                print(vh())
        elif number == '3':
            print('До свидания!')
            break
        elif number == '2':
            teach()
        else:
            print('Неверный ввод, повторите попытку')
