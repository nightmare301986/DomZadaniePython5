'''Создайте программу для игры с конфетами человек против человека.
Условие задачи: 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a. Добавьте игру против бота
b. Подумайте как наделить бота "интеллектом" '''

'''Первому  игроку  надо первым ходом забрать остаток от целочисленного деления
имеющегося количества конфет на то, которое можно взять за 1 ход максимально + 1.
В дальнейшем первому игроку нужно повторять стратегию.
Пример :  2021 % ( 28 + 1 ) = 20 , первый игрок первым ходом должен взять 20 конфет.
Если вторым ходом второй игрок взял 10 конфет, то первый должен взять 28 + 1 - 10 = 19 и так далее..
Это реализовано в игре против комьютерного бота'''

from random import *                                                              #Импорт библиотеки для псевдослучайных чисел
#import os


def sweets_player():                                                             #Реализация игры "человек с человеком"
    sweetstotal = 150
    maxhod = 28
    count1 = 0
    player1 = input('\nКак тебя зовут?: ')
    player2 = input('\nА твоего соперника?: ')

    print(f'\nНу чтож {player1} и  {player2} да начнется игра !\n')
    print('\nДля начала опеределим кто первый начнет игру.\n')

    x = randint(1, 2)                                                             #Определение кто ходит первым
    if x == 1:
        fhod = player1
        shod = player2
    else:
        fhod = player2
        shod = player1
    print(f'Поздравляю {fhod} ты ходишь первым !')

    while sweetstotal > 0:                                                         #Цикл хода игры
        if count1 == 0:
            step = int(input(f'\n Ходи {fhod} = '))                                #Ход игрока который начал первым
            if step > sweetstotal or step > maxhod:
                step = int(input(
                    f'\nМожно взять только {maxhod} конфет {fhod}, попробуй еще раз: '))
            sweetstotal = sweetstotal - step
        if sweetstotal > 0:
            print(f'\nНа кону еще {sweetstotal}')
            count1 = 1
        else:
            print('Все кончились конфеты')

        if count1 == 1:
            step = int(input(f'\n Ходи {shod} = '))                                #Ход игрока который начал вторым
            if step > sweetstotal or step > maxhod:
                step = int(input(
                    f'\nМожно взять только {sweetstotal} конфет {shod}, попробуй еще раз: '))
            sweetstotal = sweetstotal - step
        if sweetstotal > 0:
            print(f'\nНа кону еще {sweetstotal}')
            count1 = 0
        else:
            print('Конфеты кончились ')

    if count1 == 1:                                                                #Определение победителя
        print(f'{shod} ПОБЕДА!')
    if count1 == 0:
        print(f'{fhod} ПОБЕДА!')

def sweetsbot():
    sweetstotal = 150
    maxhod = 28
    player1 = input('\nКак тебя зовут?: ')
    player2 = 'Компьютер'
    players = [player1, player2]
    print(f'\nНу чтож {player1} и  {player2} да начнется игра !\n')
    print('\nДля начала определим кто первый начнет игру.\n')

    fhod = randint(-1, 0)                                                    #Определение кто ходит первым

    print(f'Поздравляю {players[fhod+1]} ты ходишь первым !')
#\n{choice(message)}: {choice(message)}
    while sweetstotal > 0:
        fhod += 1

        if players[fhod % 2] == 'Компьютер':
            print(
                f'\nХодит {players[fhod%2]} \nНа кону {sweetstotal}.  ')

            if sweetstotal < 29:                                              #Алгоритм подсчета хода для компьютера
                step = sweetstotal
            else:
                sledhod = sweetstotal//28
                step = sweetstotal - ((sledhod*maxhod)+1)
                if step == -1:
                    step = maxhod -1
                if step == 0:
                    step = maxhod
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nНу чтож ходи,  {players[fhod%2]} \nНа кону {sweetstotal} :  '))
            while step > maxhod or step > sweetstotal:                                #Информация о кол-ве конфет
                step = int(input(f'\nЗа один ход можно взять {maxhod} конфет, попробуй еще раз: '))
        sweetstotal = sweetstotal - step

    print(f'На кону осталось {sweetstotal} \nПОБЕДИЛ {players[fhod%2]}')
print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n' +
      'Первый ход определяется жеребьёвкой. '+
      'За один ход можно забрать не более чем 28 конфет. \n'+
      'Все конфеты оппонента достаются сделавшему последний ход.')

typeofgame = int(input('Выберите тип игры: 1. Игрок vs Игрок 2.Игрок vs компьютер (введите 1 или 2): '))

if typeofgame == 1:
    sweets_player()                                                             #Реализация игры "человек с компьютером"
if typeofgame == 2:
    sweetsbot()
if (typeofgame != 1) and (typeofgame != 2):
    print('Такого вида игры не существует. Перезапустите игру ')
    exit()