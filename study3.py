"""Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат."""


def checkPredicate():
    x = input("Введите значение X: ")
    y = input("Введите значение Y: ")
    z = input("Введите значение Z: ")
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    if result == True:
        print(f"Утверждение истинно")
    else:
        print(f"Утверждение ложно")
        
if __name__ == "__main__":
    checkPredicate()