# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from functools import reduce
n = int(input('Введите число N ')) 
a = int(input('Вы хотите умножить число (введите позицию числа) ')) 
b = int(input('на число (введите позицию числа) ')) 

def Result(n,a,b):
    list_1 = []

    for i in range(-n,n+1):
        list_1.append(i)
    print(list_1)

    return(list_1[a]*list_1[b])

print(Result(n,a,b))

