# Импортируем модуль для случайных чисел
import random  

# Функция раздачи карт (возвращает случайное число от 2 до 11)
def deal_card():
    return random.randint(2, 11)

# Функция подсчета очков с проверкой на перебор
def calculate_score(cards):
    if sum(cards) > 21: 
        # если сумма больше 21, возвращаем 0 
        return 0  
    # если перебора нет, возвращаем всю сумму карт
    return sum(cards)  

# Основная функция игры
def blackjack():
    print("Добро пожаловать в игру 21 очко!")
    
    # Начальная раздача карт
    # Игрок получает 2 сгенерированные карты
    player_cards = [deal_card(), deal_card()]
    # Дилер получает 1 сгенерированную карту  
    dealer_cards = [deal_card()]  
    
    print(f"Ваши карты: {player_cards}, сумма: {sum(player_cards)}")
    # обращаемся к элементу 0 массива, чтобы вывести в виде числа
    print(f"Карта дилера: {dealer_cards}")
    
    # Ход игрока 
    player_score = calculate_score(player_cards)
    # Пока у игрока нет перебора
    while player_score != 0:  
        answer = input("Хотите взять еще карту? (да/нет): ").lower()
        # Если игрок хочет взять карту, генерируем ещё одну и пересчитываем очки
        if answer == "да":
            player_cards.append(deal_card())  
            player_score = calculate_score(player_cards)  
            print(f"Ваши карты: {player_cards}, сумма: {sum(player_cards)}")

            # Если после добавления карты перебор, выходим из цикла 
            if player_score == 0:  
                print("Перебор! Вы проиграли.")
                break  
        # если игрок не отвечает "да", выходим из цикла с текущими значениями  
        else:
            break
    
    # Ход дилера (только если у игрока не было перебора)
    if player_score != 0:  
        # Дилер открывает вторую карту
        dealer_cards.append(deal_card())
        print(f"Карты дилера: {dealer_cards}, сумма: {sum(dealer_cards)}")
        
        # Дилер берет карты, пока сумма меньше 17
        while sum(dealer_cards) < 17:
            dealer_cards.append(deal_card())
            print(f"Дилер взял карту. Его карты: {dealer_cards}, сумма: {sum(dealer_cards)}")
        
        # Считаем очки дилера
        dealer_score = calculate_score(dealer_cards)  
        
        # Определение победителя
        if dealer_score == 0:
            print("У дилера перебор! Вы выиграли!")
        elif player_score > dealer_score:
            print(f"Вы выиграли! {player_score} против {dealer_score}")
        elif player_score < dealer_score:
            print(f"Дилер выиграл! {dealer_score} против {player_score}")
        else:
            print(f"Ничья! {player_score} против {dealer_score}")
    
    # Предложение сыграть еще раз
    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    if play_again == 'да':
        blackjack()  # Рекурсивный вызов для новой игры
    else:
        print("Спасибо за игру!")

# Запуск игры при прямом выполнении файла
if __name__ == "__main__":
    blackjack()