# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 100 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

# если ходить первым и брать 13 конфет (при условии, что дано 100), то выиграешь

def candy_game(candy):
    lottery = randint(0, 1)
    if lottery == 1:
        print('ходит ПЕРВЫЙ игрок')
        first_p = int(input('(PLAYER1) возьмите от 1 до 28 конфет: '))
        candy -= first_p
    else:
        print('ходит ВТОРОЙ игрок')
        second_p = int(input('(PLAYER2) возьмите от 1 до 28 конфет: '))
        candy -= second_p
    print(f'конфет осталось: {candy}')
    while candy > 0:
        if lottery == 0:
            first_p = int(input('(PLAYER1) возьмите от 1 до 28 конфет: '))
            candy -= first_p
            lottery += 1

        else:
            second_p = int(input('(PLAYER2) возьмите от 1 до 28 конфет: '))
            candy -= second_p
            lottery -=1
        print(f'конфет осталось: {candy}')
    else:
        if lottery == 1:
            print('выиграл ПЕРВЫЙ игрок')
        else:
            print('выиграл ВТОРОЙ игрок')
    return candy

def candy_game_bot_easy(candy):
    lottery = randint(0, 1)
    if lottery == 1:
        print('ходит ПЕРВЫЙ игрок')
        first_p = int(input('(PLAYER1) возьмите от 1 до 28 конфет: '))
        candy -= first_p
    else:
        print('ходит БОТ')
        second_p = randint(1, 28)
        print(f'бот берет конфеты: {second_p}')
        candy -= second_p
    print(f'конфет осталось: {candy}')
    while candy > 0:
        if lottery == 0:
            first_p = int(input('(PLAYER1) возьмите от 1 до 28 конфет: '))
            candy -= first_p
            lottery += 1

        else:
            if candy < 29:
                second_p = candy
                print(f'бот берет конфеты: {second_p}')  
                candy -= second_p
            else:          
                second_p = randint(1, 28)
                print(f'бот берет конфеты: {second_p}')
                candy -= second_p
            lottery -=1
        print(f'конфет осталось: {candy}')
    else:
        if lottery == 1:
            print('выиграл ПЕРВЫЙ игрок')
        else:
            print('выиграл БОТ')
    return candy

def candy_game_bot_hard(candy):
    lottery = randint(0, 1)
    flag = 0
    first_p = 0
    if lottery == 1:
        print('ходит ПЕРВЫЙ игрок')
        first_p = int(input('(PLAYER1) возьмите от 1 до 28 конфет: '))
        candy -= first_p
    else:
        print('ходит БОТ')
        second_p = 13
        print(f'бот берет конфеты: {second_p}')
        flag = 1
        candy -= second_p
    print(f'конфет осталось: {candy}')
    while candy > 0:
        if lottery == 0:
            first_p = int(input('(PLAYER1) возьмите от 1 до 28 конфет: '))
            candy -= first_p
            lottery += 1
        else:
            if candy < 29:
                second_p = candy
                print(f'бот берет конфеты: {second_p}')  
                candy -= second_p
            else:       
                if flag == 1:
                    second_p = 29 - first_p
                    print(f'бот берет конфеты: {second_p}')
                    candy -= second_p
                else:
                    second_p = candy - (candy // 29)*29
                    if second_p == 0:
                        second_p = randint(1, 28)
                    print(f'бот берет конфеты: {second_p}')
                    candy -= second_p
            lottery -=1
        print(f'конфет осталось: {candy}')
    else:
        if lottery == 1:
            print('выиграл ПЕРВЫЙ игрок')
        else:
            print('выиграл БОТ')
    return candy

candy_game(100)
candy_game_bot_easy(100)
candy_game_bot_hard(100)

