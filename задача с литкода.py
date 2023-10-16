a = list(map(int, input('Введите массив, состоящий из красных(1), белых(2) и синих(3) элементов: ').split()))
flag = True
count = [0] * 3

for x in a:
    if x not in [1, 2, 3]:
        print('Некорректный массив')
        flag = False
        break
    count[x-1] += 1

if flag:
    a_new = [1] * count[0] + [2] * count[1] + [3] * count[2]
    print(a_new)