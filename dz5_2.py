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

# если брать 13 конфет, то выиграешь

def candy_game(candy):
    zer = randint(0, 1)
    if zer == 1:
        print('ходит ПЕРВЫЙ игрок')
        first_p = int(input('(PLAYER1) возьмите от 1 до 28 конфет: '))
        candy -= first_p
    else:
        print('ходит ВТОРОЙ игрок')
        second_p = int(input('(PLAYER2) возьмите от 1 до 28 конфет: '))
        candy -= second_p
    print(f'конфет осталось: {candy}')
    while candy > 0:
        if zer == 0:
            first_p = int(input('(PLAYER1) возьмите от 1 до 28 конфет: '))
            candy -= first_p
            zer += 1

        else:
            second_p = int(input('(PLAYER2) возьмите от 1 до 28 конфет: '))
            candy -= second_p
            zer -=1
        print(f'конфет осталось: {candy}')
    else:
        if zer == 1:
            print('выиграл ПЕРВЫЙ игрок')
        else:
            print('выиграл ВТОРОЙ игрок')
    return candy

candy_game(100)