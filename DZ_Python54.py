words2 = []
schet = []
count1 = 1
string_vvod = input('Введите текст (пример: ааамммч): ')
words1 = string_vvod
words = words1.split()

def pressureRTL(words1, count1):                                # Алгоритм RLE (модуль сжатия)
    arrayw = [char for char in words1]
    arrayw.append('.')

    for i in range(len(arrayw)-1):
        if arrayw[i] == arrayw[i + 1]:
            count1 += 1
        else:
            schet.append(str(count1)) 
            schet.append(str(arrayw[i]))
            count1 = 1
    return schet

def unpressureRTL(schet):                                       # Алгоритм RLE (модуль восстановления)
    for i in range(0,(len(schet)),2):
        for j in range(int(schet[i])):
            words2.append(schet[i+1])

pressureRTL(words1,count1)

unpressureRTL(schet)

print('Введенная строка, сжатая  через RLE алгоритм: ', ''.join(schet))

print('Восстановленная (как введенная) строка из сжатой через RLE алгоритм: ', ''.join(words2))