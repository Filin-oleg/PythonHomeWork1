#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 


def CheckDayOfWeek(number):
    if 6 <= number <= 7:
        print("Это выходной день")
    elif 0 < number < 6:
        print("Это не выходной день")
    else:
        print("Введенное Вами число не обозначает день недели")

number = int(input(f"Введите число, обозначающее день недели: "))
CheckDayOfWeek(number)
