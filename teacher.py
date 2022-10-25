from viewer import view_homework as vh
from viewer import view_shedule as vs
from homework import add_work as aw
from homework import delete as dl

def teach():
    print('============================================')
    print('1. Посмотреть расписание')
    print('2. Посмотреть домашнее задание')
    print('3. Добавить домашнее задание')
    print('4. Удалить домашнее задание')
    print('============================================')
    num = input('Выберете пункт меню: ')


    if num == '1':
        print(vs())
    if num == '2':
        print(vh())
    if num == '3':
        aw()
    if num == '4':
        dl()