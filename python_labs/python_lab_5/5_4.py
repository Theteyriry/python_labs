import numpy as np
import matplotlib.pyplot as plt

# создаём матрицу 5×5 случайных целых чисел от 1 до 10 включительно (как в задании 3)
matrix = np.random.randint(1, 11, size=(5, 5))

# создаём новую фигуру (холст) размером 6×5
plt.figure(figsize=(6, 5))

# отображаем матрицу как тепловую карту
# cmap — цветовая карта (например 'viridis', 'plasma', 'hot' и т.д.)
# aspect='equal' — чтобы ячейки были квадратными
im = plt.imshow(matrix, cmap='viridis', aspect='equal')

# добавляем цветовую шкалу справа от карты (подпись значений цвета)
plt.colorbar(im)

# подписываем каждую ячейку её значением
# используем координаты (j, i): j — столбец (x), i — строка (y)
# цвет текста выбираем контрастным: белый если значение больше половины максимума, иначе чёрный
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        plt.text(
            j,                 # x координата по оси X в координатах данных
            i,                 # y координата по оси Y в координатах данных
            str(matrix[i, j]),        # s текст, который будет отображён. Конвертируем число matrix[i,j] в строку, чтобы его показать
            ha='center',          # ha (horizontalalignment) — горизонтальное выравнивание текста
            va='center',          # va (verticalalignment) — вертикальное выравнивание текста
            color='white' if matrix[i, j] > matrix.max() / 2 else 'black'      #    вычисляет порог matrix.max()/2 (половина максимального значения), если текущее значение > порога — текст белый ('white'), иначе — чёрный ('black').
            )

# подпись осей
plt.xlabel('Столбец')
plt.ylabel('Строка')

# заголовок графика
plt.title('Тепловая карта матрицы 5×5')

# подписываем метки по осям (0..4)
plt.xticks(range(matrix.shape[1]))
plt.yticks(range(matrix.shape[0]))

# отображаем тепловую карту в окне
plt.show()