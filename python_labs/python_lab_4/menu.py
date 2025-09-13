from tictactoe import tictactoe
from guess_number import guess_number
from blackjack import blackjack

def display_menu():
    print('='*40)
    print('1. Угадай число')
    print('2. Блэкджек (21 очко)')
    print('3. Крестики-нолики')
    print('0. Выход')
    print('='*40)

def main():
    print('Добро пожаловать в игровой клуб!')
    
    while True:
        display_menu()
        choice = input('Выберите игру (0-3): ').strip()
        
        if choice == '1':
            print('\nЗапускаем "Угадай число"...')
            guess_number()
        elif choice == '2':
            print('\nЗапускаем "Блэкджек"...')
            blackjack()
        elif choice == '3':
            print('\nЗапускаем "Крестики-нолики"...')
            tictactoe()
        elif choice == '0':
            print('\nСпасибо за игру! Ждём вас снова!')
            break
        else:
            print('\nОшибка: пожалуйста, введите цифру от 0 до 3')

if __name__ == '__main__':
    main()