'''Напишите программу, удаляющую из текста все слова, содержащие ""абв"" '''
alfabet = []
string_delete = "абв"

for i in range(len(string_delete)):
    alfabet.append(string_delete[i])

string_vvod = input('Введите текст: ')

words = string_vvod.lower().replace(",","").replace(".","").split()

print(words)

print(alfabet)

res = [words for words in words if string_delete not in words]     #Удаление слов, которые содержат слог (последовательность букв) "абв"

print(str(' '.join(res)))