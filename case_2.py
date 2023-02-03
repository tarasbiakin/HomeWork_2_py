# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

cyber = int(input("введите число "))

def Facterial(c):
  
    factorial=1
    i = 1
    while  i < cyber+1:
        factorial = factorial*i
        i= i+1
    return factorial

print(Facterial(cyber))
