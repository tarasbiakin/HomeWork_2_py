# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Введите размер списка ')) 

def List(n):
    list_1 = []
    
    for i in range(-n,n+1):
        list_1.append(i)
    return list_1
    
def ListShuf(n):
    list_1 = []
    
    for i in range(-n,n+1):
        list_1.append(i)
    random.shuffle(list_1)
    return list_1
    



print(f'Исходный список{List(n)}')

print(f'Перемешанный список{ListShuf(n)}')
