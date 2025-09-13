import random
import datetime

def save_statistics(start_time, game_time, attempts, number):
    with open("statistics.txt", "a", encoding="utf-8") as file:
        file.write(f"Время начала игры: {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Длительность игры: {game_time}\n")
        file.write(f"Количество попыток: {attempts}\n")
        file.write(f"Загаданное число: {number}\n")
        file.write("-" * 50 + "\n")  # Разделитель между играми

#создаем функцию игры "Угадай число" с сохранением статистики
def guess_number():
    #загаданное число - случайное от 1 до 100
    number = random.randint(1, 100)
    #считаем попытки (до начала игры 0 попыток)
    attempts = 0
    #сохраняем время начала игры
    start_time = datetime.datetime.now()
    #выводим приветствие 
    print("Угадай число от 1 до 100")
    
    #основной цикл игры - бесконечный (пока пользователь не угадает загаданное число)
    while True:
        try:
            #переменная "предположение" - значение, введенное пользователем
            guess = int(input("Введите число: "))
            #после ввода увеличиваем число попыток на 1
            attempts += 1
            
            #если введенное число меньше загаданного, выводим подсказку
            if guess < number:
                print("Нет, больше!")
            #второе условие - если меньше
            elif guess > number:
                print("Нет, меньше!")
            #если загаданное равно введенному, записываем время в переменную end_time
            else:
                end_time = datetime.datetime.now()
                #время игры - разность между концом и стартом
                game_time = end_time - start_time
                #выводим сообщение об окончании тура игры
                print("Поздравляю, верно!")
                #выводим данные статистики
                print(f"Ты угадал за {game_time} (попыток: {attempts})")
                # Сохраняем статистику в файл
                save_statistics(start_time, game_time, attempts, number)
                break
        except ValueError:
            print("Ты ввёл не число!")
    #спрашиваем пользователя, хочет ли он продолжить игру (делаем ответ нечувствительным к регистру)
    answer = input("Сыграем снова? (да/нет): ").lower()
    #если ответ да, снова запускаем игру
    if answer == "да":
        print("Хорошо, начинаем!")
        guess_number()  
    #если ответ другой (не только "нет" на случай, если пользователь не может закончить игру), заканчиваем
    else:
        print("Хорошо, возвращайся ещё раз")
        return 
        
    


if __name__ == '__main__':
    print("Добро пожаловать в игру 'Угадай число'!")
    guess_number()