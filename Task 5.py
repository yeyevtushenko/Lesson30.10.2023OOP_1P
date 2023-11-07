# Створіть клас BankAccount з атрибутами balance та owner,
# а також методами deposit та withdraw для здійснення операцій з балансом.
# Реалізуйте перевірку на те, що баланс не може стати від'ємним.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance