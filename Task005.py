# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        it_OK = False
        while not it_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                it_OK = True
            except ValueError:
                print("Вы ввели не целое число или совсем не число. Повторите ввод целого числа")
    return a


def measureLength(a, b):
    length = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return length


print("Введите координаты первой точки")
firstPoint = inputNumbers(2)
print("Введите координаты второй точки")
secondPoint = inputNumbers(2)

print(f"Расстояние между введеными Вами точками в 2D пространстве = {format(measureLength(firstPoint, secondPoint), '.3f')}")