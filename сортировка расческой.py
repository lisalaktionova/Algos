a = list(map(int, input('Введите массив через пробел: ').split()))
step = len(a)

while step > 1 or flag:
    if step > 1:
        step = int(step/1.247)
    flag = False
    i = 0
    while i + step < len(a):
        if a[i] > a[i + step]:
            t = a[i]
            a[i] = a[i + step]
            a[i + step] = t
            flag = True
        i += step

print(*a)