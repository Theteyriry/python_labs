import numpy as np
import matplotlib.pyplot as plt

# создаём массив x: 100 чисел от 0 до 10 включительно
x = np.linspace(0, 10, 100)

# вычисляем sin для каждого значения x (в радианах)
y = np.sin(x)
# вычисляем cos для каждого значения x (в радианах)
z = np.cos(x)

# создаёт новую фигуру (холст) размером 8×5
# параметр figsize=(width, height)
plt.figure(figsize=(8, 5))


# Построение линий

# рисует график y=sin(x) как линию; label задаёт подпись для легенды
plt.plot(x, y, label='sin(x)')

# рисует график z=cos(x); тоже с подписью для легенды
plt.plot(x, z, label='cos(x)')

# подпись оси X
plt.xlabel('x')

# подпись оси Y (строка)
plt.ylabel('y')

# заголовок графика
plt.title('Графики sin(x) и cos(x)')

# отображает легенду
plt.legend()

# включает сетку
plt.grid(True)

# отображает фигуру в окне (или в ноутбуке inline)
plt.show()