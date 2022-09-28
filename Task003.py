# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def inputCoordinate(x):
    a = [0] * x
    for i in range(x):
        it_OK = False
        while not it_OK:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                it_OK = True
                if a[i] == 0:
                    it_OK = False
                    print("Координата не может быть равна 0, повторите ввод ")
            except ValueError:
                print("Вводить нужно только число!")
    return a


def checkCoordinate(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


coordinate = inputCoordinate(2)
checkCoordinate(coordinate)
