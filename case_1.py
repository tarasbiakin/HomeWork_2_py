# Задача 2: Найдите сумму цифр трехзначного числа. 

cyber = int(input("введите число "))

if cyber<99 or cyber>999:
    print('Ввели не корректное число')

def Summa(c):
    sum = 0
    while c>0:
        sum = sum+c%10
        c = c//10
    return sum

print(Summa(cyber))
# print(f'Сумма числа ={sum}')








