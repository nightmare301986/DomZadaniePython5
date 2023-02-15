'''Игра крестики-нолики. Первым начинают '0', затем 'X' и т.д. При возможных ошибках (нажал еще раз занятую клетку) выводится сообщение об ошибке.
Игрок выбирает клеточки, путем нажатия на нее курсором мыши, для своего хода . При заполнении всех клеток, если ни один игрок не добился
победы - игра сообщает: "НИЧЬЯ! Игра окончена! Больше нет ходов." Победитель также выявляется автоматически выводится сообщение о победе,
которое сообщает, что победил игрок 'X' или 'O' и игровое поле закрывается.'''

from tkinter import *                                                  #Импорт библиотек  1.Tkinter
from tkinter.messagebox import showinfo                                #                  2. Отображения сообщений

root = Tk()
root.title("ИГРА КРЕСТИКИ-НОЛИКИ")
f_top = Frame(root)
f_cent = Frame(root)
f_bot = Frame(root)

cifra = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                   #Формирование списков для работы игры
khod = [] 

global m
clicks = 1

def which_button(button_press, m):                                    #Основная функция работы игры
    global clicks
    print(clicks)                                                     #Вывод количества "кликов" по иговому полю
    if m in cifra:                                                    #Обработка повторного нажатия (хода)
        khod.append(m)
        cifra.remove(m)
    else:
        showinfo(title="Предупреждение", message="Неправильно выбрали ход")      #Сообщение об ошибке      
        return 0
    
    if clicks%2 == 0:                                                 #Отображение хода игрока "О" (хода)
        l[m]["text"] ="O"
            
    if clicks%2 != 0:                                                 #Отображение хода игрока "Х" (хода)
        l[m]["text"] ="X"

    #Обработка выигрыша игрока "О"
    if (l[1]["text"] == l[2]["text"] == l[3]["text"]=="O") or (l[4]["text"] == l[5]["text"] == l[6]["text"]=="O") or (l[7]["text"] == l[8]["text"] == l[9]["text"]=="O"):
        showinfo(title="Информация", message="ПОБЕДА ИГРОКА 'O' Игра окончена!")
        close()
        return 0
    if (l[1]["text"] == l[4]["text"] == l[7]["text"]=="O") or (l[2]["text"] == l[5]["text"] == l[8]["text"]=="O") or (l[3]["text"] == l[6]["text"] == l[9]["text"]=="O"):
        showinfo(title="Информация", message="ПОБЕДА ИГРОКА 'O' Игра окончена!")
        close()
        return 0
    if (l[1]["text"] == l[5]["text"] == l[9]["text"]=="O") or (l[3]["text"] == l[5]["text"] == l[7]["text"]=="O"):
        showinfo(title="Информация", message="ПОБЕДА ИГРОКА 'O' Игра окончена!")
        close()
        return 0

    #Обработка выигрыша игрока "Х"
    if (l[1]["text"] == l[2]["text"] == l[3]["text"]=="X") or (l[4]["text"] == l[5]["text"] == l[6]["text"]=="X") or (l[7]["text"] == l[8]["text"] == l[9]["text"]=="X"):
        showinfo(title="Информация", message="ПОБЕДА ИГРОКА 'X' Игра окончена!")
        close()
        return 0
    if (l[1]["text"] == l[4]["text"] == l[7]["text"]=="X") or (l[2]["text"] == l[5]["text"] == l[8]["text"]=="X") or (l[3]["text"] == l[6]["text"] == l[9]["text"]=="X"):
        showinfo(title="Информация", message="ПОБЕДА ИГРОКА 'X' Игра окончена!")
        close()
        return 0
    if (l[1]["text"] == l[5]["text"] == l[9]["text"]=="X") or (l[3]["text"] == l[5]["text"] == l[7]["text"]=="X"):
        showinfo(title="Информация", message="ПОБЕДА ИГРОКА 'X' Игра окончена!")
        close()
        return 0

    clicks = clicks + 1                                                       #Счетчик ходов

    if clicks == 10:                                                          #Условия окончания игры при ситуации "Ничья"
        showinfo(title="Информация", message="НИЧЬЯ! Игра окончена! Больше нет ходов.")
        close()
        return 0
       
def close():                                                                  #Обработчик закрытия поля (формы) игры
    root.destroy()
    
l = [ 1,                                                                      #Формирование игрового поля 3 на 3 на основе списка
Button(f_top, width=8, height=5,
           bg='lightblue', font="Courier 30", text="",command=lambda m = 1: which_button(m,1)),      #Клеточка 1(0) на поле
Button(f_top, width=8, height=5,
           bg='lightblue', font="Courier 30", text="",command=lambda m = 2: which_button(m,2)),
Button(f_top, width=8, height=5,
           bg='lightblue', font="Courier 30",  text="",command=lambda m = 3: which_button(m,3)),
Button(f_cent, width=8, height=5,
           bg='lightblue', font="Courier 30",  text="",command=lambda m = 4: which_button(m,4)),
Button(f_cent, width=8, height=5,
           bg='lightblue', font="Courier 30",  text="",command=lambda m = 5: which_button(m,5)),
Button(f_cent, width=8, height=5,
           bg='lightblue', font="Courier 30",  text="",command=lambda m = 6: which_button(m,6)),
Button(f_bot, width=8, height=5,
           bg='lightblue', font="Courier 30",  text="",command=lambda m = 7: which_button(m,7)),
Button(f_bot, width=8, height=5,
           bg='lightblue', font="Courier 30",  text="",command=lambda m = 8: which_button(m,8)),
Button(f_bot, width=8, height=5,
           bg='lightblue', font="Courier 30",  text="",command=lambda m = 9: which_button(m,9))
]
 
f_top.pack()                                                                   #Расстановка элементов на форме
f_cent.pack()
f_bot.pack()
l[1].pack(side=LEFT)
l[2].pack(side=LEFT)
l[3].pack(side=LEFT)
l[4].pack(side=LEFT)
l[5].pack(side=LEFT)
l[6].pack(side=LEFT)
l[7].pack(side=LEFT)
l[8].pack(side=LEFT)
l[9].pack(side=LEFT)
 
root.mainloop() 