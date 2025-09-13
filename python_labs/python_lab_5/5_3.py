import numpy as np

# создаём матрицу 5×5 случайных целых чисел от 1 до 10 включительно
# np.random.randint(low, high, size) — low включительно, high исключается, поэтому high=11
matrix = np.random.randint(1, 11, size=(5, 5))

# вычисляем среднее по всем элементам матрицы
mean_value = np.mean(matrix)

# находим максимальный элемент в матрице
max_value = np.max(matrix)

# находим минимальный элемент в матрице
min_value = np.min(matrix)

# считаем сумму по столбцам (axis=0) — возвращает массив длины 5 (по каждому столбцу)
sum_by_columns = np.sum(matrix, axis=0)

# печатаем матрицу и результаты
print("Матрица (5x5):")
print(matrix)                     # выводит саму матрицу
print("\nСреднее значение:", mean_value)
print("Макс:", max_value)
print("Мин:", min_value)
print("Сумма по столбцам:", sum_by_columns)