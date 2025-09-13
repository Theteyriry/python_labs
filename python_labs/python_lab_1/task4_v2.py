#добавляем модуль random для генерации случайных значений
import random
#обращаемся к методу randint для генерации целых чисел в заданном диапазоне 10 раз, записываем число в список
numbers = [random.randint(-1000, 1000) for i in range(10)]
print("Список чисел:", numbers)
min_n = min(numbers)
max_n = max(numbers)
summa = sum(numbers)
sorted_n = sorted(numbers)
print("Максимальное значение:", max_n)
print("Минимальное значение:", min_n)
print("Сумма чисел:", summa)
print("Список чисел по возрастанию:", sorted_n)