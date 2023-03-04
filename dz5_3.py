# Создайте программу для игры в ""Крестики-нолики"".

from random import randint

def pole(pole_list1, pole_list2, pole_list3):
    pole_list1 = '|1| |2| |3|'
    print(pole_list1)
    pole_list2 = '|4| |5| |6|'
    print(pole_list2)
    pole_list3 = '|7| |8| |9|'
    print(pole_list3)
    return pole_list1, pole_list2, pole_list3

def game(move):
    zer = randint(0, 1)
    if zer == 1:
        print('ходит ПЕРВЫЙ игрок')
        zeros = int(input('(PLAYER1 - 0) выберите позицию от 1 до 9: '))
        
        if str(zeros) in pole_list1:
            pole_list1 = pole_list1.replace(str(zeros), '0')
        elif str(zeros) in pole_list2:
            pole_list2 = pole_list2.replace(str(zeros), '0')
        elif str(zeros) in pole_list3:
            pole_list3 = pole_list3.replace(str(zeros), '0')

    else:
        print('ходит ВТОРОЙ игрок')
        crosses = int(input('(PLAYER2 - Х) ыберите позицию от 1 до 9: '))
        if str(crosses) in pole_list1:
            pole_list1 = pole_list1.replace(str(crosses), 'X')
        elif str(crosses) in pole_list2:
            pole_list2 = pole_list2.replace(str(crosses), 'X')
        elif str(crosses) in pole_list3:
            pole_list3 = pole_list3.replace(str(crosses), 'X')

    print(pole_list1)
    print(pole_list2)
    print(pole_list3)

