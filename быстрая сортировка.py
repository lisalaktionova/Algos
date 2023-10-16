from random import choice

def quicksort(a):
    if len(a) <= 1: #проверяем длину списка
        return a
    n = choice(a)
    more_a = []
    less_a = []
    mid_a = []
    for x in a:
        if x > n:
            more_a.append(x)
        elif x < n:
            less_a.append(x)
        else:
            mid_a.append(x)
    return quicksort(less_a) + mid_a + quicksort(more_a)

a = list(map(int, input('Введите массив через пробел: ').split()))
print('Отсортированный массив: ', *quicksort(a))