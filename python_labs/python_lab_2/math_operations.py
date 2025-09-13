#создаем функцию 2 переменных, возвращающих результат
def summa(a, b):
    return a+b
def raznost(a, b):
    return a-b
def umnozhenie(a, b):
    return a*b
def delenie(a, b):
    #пробуем вывести результат деления. если возникла ошибка при делении на 0, выводим сообщение
    try:
        return a/b
    except ZeroDivisionError:
        return("Ошибка: деление на 0 невозможно")
