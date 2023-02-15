'''Игра крестики-нолики. Первым начинают '0', затем 'X' и т.д. Игрокам дается 20 раундов с учетом возможных ошибок.
Игрок вводит номер клеточки для своего хода (например - 2). При заполнении всех клеток, если ни один игрок не добился
победы - игра сообщает: 'НИЧЬЯ! Все возможные ходы для игроков закончились. ' Победитель также выявляется автоматически и
игра прекращается.'''

print('Привет игрокам! Да начнется игра! У вас есть 20 раундов, чтобы сыграть друг с другом. Да победит умнейший!')

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]                                    #Подготовка поля для игры
cifra = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                      #Список для проверки ввода хода
global count1
count1 = 0

def matrix1(a):                                                          #Вывод на экран поля для игры
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j],'\t', end='')
        print()

def stepcrossnull(n, count1):                                            #Отметка хода на поле для игры (в клетках - О или Х)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if count1%2 == 0:
                if a[i][j] == n:
                    a[i][j] = 'O'
                    n2 = n
                else:
                    a[i][j] = a[i][j]
                    n2 = n
            if count1%2 == 1:
                if a[i][j] == n:
                    a[i][j] = 'X'
                    n2 = n
                else:
                    a[i][j] = a[i][j]
                    n2 = n
        n2 = n   

def stop(count1):                                                     #Определение победителя или остановки игры без победителя
    if (a[0][0] == a[1][1]) and (a[0][0] == a[2][2]):
        if count1%2 == 0:
            matrix1(a)
            print('Игра окончена. Выиграл игрок O')
            exit()
        else:
            matrix1(a)
            print('Игра окончена. Выиграл игрок X')
            exit()
    if (a[0][2] == a[1][1]) and (a[0][2] == a[2][0]):
        if count1%2 == 0:
            matrix1(a)
            print('Игра окончена. Выиграл игрок O')
            exit()
        else:
            matrix1(a)
            print('Игра окончена. Выиграл игрок X')
            exit()
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (a[i][j] == a[i][j+1]) and (a[i][j] == a[i][j+2]):
                if count1%2 == 0:
                    matrix1(a)
                    print('Игра окончена. Выиграл игрок O')
                    exit()
                else:
                    matrix1(a)
                    print('Игра окончена. Выиграл игрок X')
                    exit()
            else:
                break
    for j in range(len(a)):
        for i in range(len(a[i])):
            if (a[i][j] == a[i+1][j]) and (a[i][j] == a[i+2][j]):
                if count1%2 == 0:
                    matrix1(a)
                    print('Игра окончена. Выиграл игрок O')
                    
                    exit()
                else:
                    matrix1(a)
                    print('Игра окончена. Выиграл игрок X')
                    
                    exit()
            else:
                break
    if  count1 >= 8:
        print('НИЧЬЯ! Все возможные ходы для игроков закончились. ')
        matrix1(a)   
        exit()

def proverka(n, count1):                                                  #Проверка значения введенной цифры хода
    if n in cifra:
        count1 += 1
        cifra.remove(n)
        print(cifra)
        return count1
    else:
        print('ОШИБКА ХОДА! Проверьте свой ход и введите ЗАНОВО значение хода')
        return count1
    

for h in range(20):                                                       #Игра. С расчетом, что имеется 20 раундов
    matrix1(a) 
    if count1%2 == 0:
        name_player = 'игрок O  '
    if count1%2 != 0:
        name_player = 'игрок X  '
    n = int(input('Введите номер клетки '+ name_player  ))
    if h >= 10:
        print('У вас осталось возможных ходов', 20-h ,' через которые игра закончится.') #Предупреждение о количестве возможных раундов игры
    if h == 19:
        print('Все возможные ходы закончились. Доигрались...')

    stepcrossnull(n, count1)                                                #Вызов функций игры
    stop(count1)
    count1 = proverka(n,count1)
    print(count1)

matrix1(a)   
