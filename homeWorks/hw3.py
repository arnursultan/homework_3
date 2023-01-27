class Bank:
    def __init__(self, __name) -> None:
        self.__name = __name
        self.__balance = 0
    def money_x(self):
        user = int(input('Сколько денег хотите положить на баланс?: '))
        self.__balance += user
        return f'На вашем счете {self.__balance}, Имя владельца: {self.__name}'
    def _kill(self):
        user = int(input('Сколько денег хотите обналичить?: '))
        if user >= 0:
            self.__balance -= user
            return f'Вы обналичили счет на {user},Остаток на карте: {self.__balance}'
        else:
            return f'На вашем счете недостаточно средств: {self.__balance}'
    def __jackpot(self):
        return f'Ваш счет умножен на 10 раз, Ваш счет: {self.__balance * 10}'
    def user(self, name, __balancce):
        self.name = name
        self.__balancce = __balancce
        return f'Имя: {self.name}, Баланс: {self.__balancce + self.__balance}'
ban = Bank('Айжан')
print(ban.money_x())
print(ban._kill())
print(ban.user('Бекболот',100))
print(ban._Bank__jackpot())