"""Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным."""

def checkNumber():
    while True:
        num = int(input("Введите число: "))
        if 6 <= num <= 7:
            print("Yes")
        elif 0 < num < 6:
            print("No")
        else:
            print("число вне пределов 7 дней")

if __name__ == "__main__":
    checkNumber()