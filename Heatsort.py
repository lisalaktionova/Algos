import math

mas=list(map(int,input("Введите элементы массива: ").split()))

ans=list() # 'будущий' отсортированный массив
def hsort(mas): # функция для одного перебора дерева
    l=len(mas) #длина массива
    level= int(math.log2(7))+1 #кол-во уровней
    i=0 # индекс для перебора переменных (троек)
    stepen=1 # текущий уровень
    k=0 # счетчик для кол-ва рассмотренных элементов на уровне
    move=0 # счетчик перестановок в массиве
    ind=2**stepen-1 # индекс второго элемента из тройки сравниваемых
    while ind<l and stepen<level: #ищем макс в тройках
        if ind+1<l: # смотрим, что в тройке 3 элемента, а не 2
            temp=max(mas[i],mas[ind],mas[ind+1])
            if temp!=mas[i]:
                move+=1
                if temp==mas[ind]:
                    mas[i],mas[ind]=mas[ind],mas[i]
                else:
                    mas[i],mas[ind+1]=mas[ind+1],mas[i]
        else: # если в тройке 2 элемента
            temp=max(mas[i],mas[ind])
            if temp!=mas[i]:
                move+=1
                mas[i],mas[ind]=mas[ind],mas[i]
        i+=1 # берем тройку для следующего элемента
        k+=2 # на два, т.к. рассмотрели пару элементов текущего уровня
        ind+=2
        if k==(2**(stepen-1)): # если на уровне все элементы пройдены, то переходим на следующий уровень
            stepen+=1
            ind=2**stepen-1
            k=0 # обнуляем счетчик для нового уровня
    if move==0: # если в массиве ничего не меняется, значит max в начале массива (отсортированное дерево)
        ans.append(mas[0])
        mas.remove(mas[0])

def cutmas(m): # сортируем, пока не отсортируется
    while len(mas)>2:
        hsort(mas)
        #print(mas)
        #print(ans)
    temp=max(mas[0],mas[1])
    if temp==mas[0]:
        ans.append(mas[0])
        ans.append(mas[1])
    else:
        ans.append(mas[1])
        ans.append(mas[0])

cutmas(mas)
print(ans)




