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

def combsort(a):
    step = len(a)

    while step > 1 or flag:
        if step > 1:
            step = int(step / 1.247)
        flag = False
        i = 0
        while i + step < len(a):
            if a[i] > a[i + step]:
                t = a[i]
                a[i] = a[i + step]
                a[i + step] = t
                flag = True
            i += step

    return a

import timeit
import random

time_q, time_c = 0, 0
for i in range(100):
    # a = list(map(int, input('Введите массив через пробел: ').split()))
    a = [random.randint(0, 100) for _ in range(100)]
    time_q += timeit.timeit('[quicksort]', globals=globals())
    time_c += timeit.timeit('[combsort]', globals=globals())
print('Примерное время выполнения быстрой сортировки: ', time_q / 100)
print('Примерное время выполнения сортировки расческой: ', time_c / 100)
