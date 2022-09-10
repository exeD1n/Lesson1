"""Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве."""

def calculateLengthSegment():
    print("Введите координату по A")
    aA = int(input(f"Введите координату по X: "))
    aB = int(input(f"Введите координату по Y: "))
    print("Введите координату по B")
    bA = int(input(f"Введите координату по X: "))
    bB = int(input(f"Введите координату по Y: "))
    lengthSegment = ((bA - aA) ** 2 + (bB - aB) ** 2) ** (0.5)
    print(f"Длина отрезка: {lengthSegment}")
    
if __name__ == "__main__":
    calculateLengthSegment()