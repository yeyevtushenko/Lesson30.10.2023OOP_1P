# Створіть клас BankAccount з атрибутами balance та owner,
# а також методами deposit та withdraw для здійснення операцій з балансом.
# Реалізуйте перевірку на те, що баланс не може стати від'ємним.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Поповнення балансу на {amount} грн успішно виконано.")
        else:
            print("Помилка: Сума поповнення повинна бути більше нуля.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Виведення {amount} грн успішно виконано.")
            else:
                print("Помилка: Недостатньо коштів на балансі.")
        else:
            print("Помилка: Сума виведення повинна бути більше нуля.")

    def display_balance(self):
        print(f"Баланс на рахунку користувача {self.owner}: {self.balance} грн")

account = BankAccount("Олег Олексійович", 15000)
# Перевіримо код на правильність виконання
account.display_balance()
account.deposit(500)
account.display_balance()
account.withdraw(3000)
account.display_balance()
# Перевірка виведення більше, ніж є на рахунку
account.withdraw(15000)