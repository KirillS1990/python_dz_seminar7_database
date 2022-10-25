def view_homework():
    with open("homework.txt", 'r') as file:
        hw = file.read()
        return hw


def view_shedule():
    with open("shedule.txt", 'r') as file:
        sc = file.read()
        return sc