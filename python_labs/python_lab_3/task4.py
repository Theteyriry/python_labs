class BankAccount:
    #устанавливаем баланс по умолчанию 0
    def __init__(self, initial_balance=0):
        #нижним подчеркиванием обозначаем приватность атрибута
        self._balance = initial_balance
        self._transactions = []
        # Записываем начальный баланс как первую транзакцию
        self._transactions.append(f"Начальный баланс: {initial_balance}")
    
    #добавляем функцию пополнения счета
    def deposit(self, amount):
        #если сумма 0 или меньше, выводим ошибку (с балансом и транзакциями ничего не происходит)
        if amount <= 0:
            print("Ошибка: сумма пополнения должна быть больше 0")
        else:
            #увеличиваем баланс на сумму пополнения
            self._balance = self._balance + amount
            #записываем операцию
            self._transactions.append(f"Пополнение: +{amount}. Баланс: {self._balance}")
            #сообщаем об успешности операции
            print(f"Счет пополнен на {amount}. Текущий баланс: {self._balance}")
    
    #добавляем функцию снятия со счета
    def withdraw(self, amount):
        #если сумма 0 или меньше, выводим ошибку (ничего не происходит)
        if amount <= 0:
            print("Ошибка: сумма должна быть больше 0")
        #если сумма больше баланса, выводим ошибку (добавляем транзакцию)
        if amount > self._balance:
            print(f"Ошибка: недостаточно средств. Текущий баланс: {self._balance}")
            self._transactions.append(f"Неудачная попытка снятия {amount}. Баланс: {self._balance}")
        else:
            #уменьшаем баланс на сумму снятия
            self._balance = self._balance - amount
            #добавляем транзакцию 
            self._transactions.append(f"Снятие: -{amount}. Баланс: {self._balance}")
            #уведомляем об успешности операции
            print(f"Со счета снято {amount}. Текущий баланс: {self._balance}")
    
    #используем геттер для работы с приватными атрибутами
    @property
    #property превратил метод в атрибут, то есть ничего не делает со значениями
    def balance(self):
        return self._balance
    
    def get_transaction_history(self):
    #не используем геттер, тк выводим только копию, а оригинальный список транзакций защищаем от изменений
        return self._transactions.copy()  

# Демонстрация работы класса
if __name__ == "__main__":
    # Создаем банковский счет с начальным балансом 1000
    account = BankAccount(1000)
    print(f"Начальный баланс: {account.balance}")
    
    # Пополняем счет
    account.deposit(500)
    
    # Снимаем средства
    account.withdraw(200)
    
    # Пытаемся снять слишком много
    account.withdraw(2000)
    
    # Пытаемся внести отрицательную сумму
    account.deposit(-100)
    
    # Выводим историю транзакций
    print("\nИстория транзакций:")
    for transaction in account.get_transaction_history():
        print(transaction)
    
    # Показываем текущий баланс через геттер
    print(f"\nТекущий баланс: {account.balance}")