# Створіть клас Circle з атрибутом radius та методом area,
# який поверне площу кола з вказаним радіусом.
print("Завдання №2")
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


radius = float(input("Введіть радіус кола: "))
circle = Circle(radius)
circle_area = circle.area()
print(f"Площа кола з радіусом {circle.radius} дорівнює {circle_area:.2f}")