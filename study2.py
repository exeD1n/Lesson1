"""Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится)."""


def checkCoordinates():
    xy = float(input(f"Введите Y координату: "))
    yx = float(input(f"Введите X координату: "))
    text = 4
    if xy > 0 and yx > 0:
        text = 1
    elif xy < 0 and yx > 0:
        text = 2
    elif xy < 0 and yx < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


if __name__ == "__main__":
    checkCoordinates()