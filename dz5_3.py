# Создайте программу для игры в ""Крестики-нолики"".

from random import randint

def pole_print(pole_list1, pole_list2, pole_list3):
    print(pole_list1)
    print(pole_list2)
    print(pole_list3)
    return pole_list1, pole_list2, pole_list3

def game(move):
    pole_list1 = '|1| |2| |3|'
    pole_list2 = '|4| |5| |6|'
    pole_list3 = '|7| |8| |9|'

    pole_print(pole_list1, pole_list2, pole_list3)
    flag = 0
    winner = ''
    while flag == 0:
        if move == 1:
            print('ходит ПЕРВЫЙ игрок')
            zeros = int(input('(PLAYER1 - 0) выберите позицию от 1 до 9: '))

            if str(zeros) in pole_list1:
                pole_list1 = pole_list1.replace(str(zeros), '0')
            elif str(zeros) in pole_list2:
                pole_list2 = pole_list2.replace(str(zeros), '0')
            elif str(zeros) in pole_list3:
                pole_list3 = pole_list3.replace(str(zeros), '0')

            move -= 1
            pole_print(pole_list1, pole_list2, pole_list3)

            if pole_list1 == '|0| |0| |0|' or pole_list2 == '|0| |0| |0|' or pole_list3 == '|0| |0| |0|' or (pole_list1[1] == '0' and pole_list2[1] =='0' and pole_list3[1] == '0') or (pole_list1[5] == '0' and pole_list2[5] =='0' and pole_list3[5] == '0') or (pole_list1[9] == '0' and pole_list2[9] =='0' and pole_list3[9] == '0') or (pole_list1[1] == '0' and pole_list2[5] =='0' and pole_list3[9] == '0') or (pole_list1[9] == '0' and pole_list2[5] =='0' and pole_list3[1] == '0'):
                winner = 'НОЛИКИ'
                print(f'ПОБЕДИЛ игрок - {winner}')
                flag = 1
            elif pole_list1 == '|X| |X| |X|' or pole_list2 == '|X| |X| |X|' or pole_list3 == '|X| |X| |X|' or (pole_list1[1] == 'X' and pole_list2[1] =='X' and pole_list3[1] == 'X') or (pole_list1[5] == 'X' and pole_list2[5] =='X' and pole_list3[5] == 'X') or (pole_list1[9] == 'X' and pole_list2[9] =='X' and pole_list3[9] == 'X') or (pole_list1[1] == 'X' and pole_list2[5] =='X' and pole_list3[9] == 'X') or (pole_list1[9] == 'X' and pole_list2[5] =='X' and pole_list3[1] == 'X'):
                winner = 'КРЕСТИКИ'
                print(f'ПОБЕДИЛ игрок - {winner}')
                flag = 1
            elif pole_list1[1] != '1' and pole_list1[5] != '2' and pole_list1[9] != '3' and pole_list2[1] != '4' and pole_list2[5] != '5' and pole_list2[9] != '6' and  pole_list3[1] != '7' and pole_list3[5] != '8' and pole_list3[9] != '9':
                winner = 'НИЧЬЯ'
                print(winner)
                flag = 1 

        else:
            print('ходит ВТОРОЙ игрок')
            crosses = int(input('(PLAYER2 - Х) выберите позицию от 1 до 9: '))
            if str(crosses) in pole_list1:
                pole_list1 = pole_list1.replace(str(crosses), 'X')
            elif str(crosses) in pole_list2:
                pole_list2 = pole_list2.replace(str(crosses), 'X')
            elif str(crosses) in pole_list3:
                pole_list3 = pole_list3.replace(str(crosses), 'X')

            move += 1
            pole_print(pole_list1, pole_list2, pole_list3)

            if pole_list1 == '|0| |0| |0|' or pole_list2 == '|0| |0| |0|' or pole_list3 == '|0| |0| |0|' or (pole_list1[1] == '0' and pole_list2[1] =='0' and pole_list3[1] == '0') or (pole_list1[5] == '0' and pole_list2[5] =='0' and pole_list3[5] == '0') or (pole_list1[9] == '0' and pole_list2[9] =='0' and pole_list3[9] == '0') or (pole_list1[1] == '0' and pole_list2[5] =='0' and pole_list3[9] == '0') or (pole_list1[9] == '0' and pole_list2[5] =='0' and pole_list3[1] == '0'):
                winner = 'НОЛИКИ'
                print(f'ПОБЕДИЛ игрок - {winner}')
                flag = 1
            elif pole_list1 == '|X| |X| |X|' or pole_list2 == '|X| |X| |X|' or pole_list3 == '|X| |X| |X|' or (pole_list1[1] == 'X' and pole_list2[1] =='X' and pole_list3[1] == 'X') or (pole_list1[5] == 'X' and pole_list2[5] =='X' and pole_list3[5] == 'X') or (pole_list1[9] == 'X' and pole_list2[9] =='X' and pole_list3[9] == 'X') or (pole_list1[1] == 'X' and pole_list2[5] =='X' and pole_list3[9] == 'X') or (pole_list1[9] == 'X' and pole_list2[5] =='X' and pole_list3[1] == 'X'):
                winner = 'КРЕСТИКИ'
                print(f'ПОБЕДИЛ игрок - {winner}')
                flag = 1
            elif pole_list1[1] != '1' and pole_list1[5] != '2' and pole_list1[9] != '3' and pole_list2[1] != '4' and pole_list2[5] != '5' and pole_list2[9] != '6' and  pole_list3[1] != '7' and pole_list3[5] != '8' and pole_list3[9] != '9':
                winner = 'НИЧЬЯ'
                print(winner)
                flag = 1 
    return winner

lottery = randint(0, 1)
game(lottery)