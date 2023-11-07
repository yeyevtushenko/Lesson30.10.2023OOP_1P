# Створіть клас Student з атрибутами name та age.
# Додайте метод print_info, який виведе інформацію про студента у на вигляді
# "Ім'я: {name}, Вік: {age}".
print("Завдання №1")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")


student = Student("Олег", 17)

student.print_info()