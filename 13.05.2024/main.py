# D8:2, D7:3, D5:3,D2:2

# D2:2
n = int(input())
s = ''
while n >0:
    q = n %8
    s = str(q) + s
    n = n//8
print(s)

# D5:3
n = input('Parol daxil et: ')
nl = len(n)
b = []
for i in n:
    if b.count(i) == 0:
        b.append(i)
bl = len(b)
if nl >= 10 and bl >= 4:
    print('Təhlükəsiz paroldur')
else:
    print('Tehlukeli paroldur')

# D7:3
n = int(input())
n = str(n)
ln = len(n)
f = 0
for i in range(0, ln):
    if n[0] == n[i]:
        f = 1
    else:
        f = 0
if f == 1:
    print('Beli')
else:
    print('Xeyr')

# D8:2

n = int(input())
k = 0
i = 2
while i <= n//2:
    if n%i==0:
        k = k+1
    i = i+1
k=k+1
print(k)

