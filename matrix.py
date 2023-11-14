n=int(input('Введите количество матриц: '))
p=list() #список для хранения кол-ва столбцов/строк
ans=''
for i in range(n):
    a=list(map(int,input().split()))
    if i==0:
        p.append(a[0])
        p.append(a[1])
    else:
        p.append(a[1])

m=[[10**10]*(n+1) for i in range(n+1)] #массив для произведений матриц
for i in range(1,n+1):
    m[i][i]=0
s=[[0]*(n+1) for i in range(n+1)] #оптимальное умножение

def mult(i,j):
    if m[i][j]==10**10:
        for k in range(i,j):
            temp=mult(i,k)+mult(k+1,j)+p[i-1]*p[k]*p[j]
            if temp<m[i][j]:
                m[i][j]=temp
                s[i][j]=k
    return m[i][j]

def pr(i,j):
    if i==j:
        return 'A'+str(i)
    return '('+pr(i,s[i][j])+'x'+pr(s[i][j]+1,j)+')'

mult(1,n)
ans=pr(1,n)
print(ans)