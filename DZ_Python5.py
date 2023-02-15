'''Напишите программу, удаляющую из текста все слова, содержащие (любые, т.е. с хотя бы одной буквой а или б или в) ""абв"" '''
alfabet = []
string_delete = "абв"

for i in range(len(string_delete)):
    alfabet.append(string_delete[i])

string_vvod = input('Введите текст: ')

words = string_vvod.lower().replace(",","").replace(".","").split()

print(words)

print(alfabet)

res = [ele for ele in words if all(ch not in ele for ch in alfabet)]   #Удаление слов, которые содержат одну из букв: "а", "б" или "в"

print(str(' '.join(res)))