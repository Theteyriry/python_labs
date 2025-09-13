# Создаем пустой список для хранения чисел
numbers = []  
# Открываем файл в режиме чтения
with open('data.txt', 'r') as file:  
    #читаем файл построчно  
    for line in file:
        #преобразуем строку в целое число 
        n = int(line.strip())  
        #добавляем полученное число в список
        numbers.append(n)
   
#с помощью встроенных функций вычисляем минимальное и максимальное значение, их сумму и ср. арифметическое
summa = sum(numbers)  
avr = summa/ len(numbers)  
max_n = max(numbers)  
min_n = min(numbers)  

# открываем (или создаем, если нет) файл в режиме записи
with open('result.txt', 'w') as file: 
    #записываем фразу "сумма" и значение переменной, переходим на новую строку (/n) 
    file.write(f"Сумма: {summa}\n") 
    file.write(f"Среднее: {avr}\n")
    file.write(f"Максимум: {max_n}\n")
    file.write(f"Минимум: {min_n}\n")
print("Результат записан в файл result.txt")