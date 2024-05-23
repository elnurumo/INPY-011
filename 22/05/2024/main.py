

# def f(x):
#     p = 1
#     for i in range(1,x):
#         p = p+x
#     return p
# ls = [5,1,3,7,2,12]
# s = 0
# for i in ls:
#     if f(i) < 16:
#         s = s + i
# print(s)

# for i in range(1,1):
#     print(i)

# 84

# a = [3,4,2,1,6,9,7,8,12,10,5,14]
# cəm = 0
# say = 0
# for i in range(0,len(a)):
#     if a[i] % 2 == 0 and i % 2 != 0:
#         say = say + 1
#         cəm = cəm + a[i]
#     elif a[i] % 2 != 0 and  i % 2 == 0:
#         say = say + 1
#         cəm = cəm + a[i]
# edediorta = cəm/say
# print(edediorta)

# 86
# 1
# n = float(input())
# if n > 0:
#     a = int(n)
#     q = n - a
# elif n < 0:
#     a = int(n) - 1
#     q = n - a
# print(a,q)

# 2
# n = input()
# for i in range(0,len(n)):
#     if float(n) > 0:
#         if n[i] == '.':
#             t = n[0:i]
#             q = '0' + n[i:]
#     elif float(n) < 0:
#         if n[i] == '.':
#             t = int(n[0:i]) - 1
#             q = 1 - float('0' + n[i:])
# print(t,q)

# 89
# n = int(input())
# s = 0
# f = 1
# k = -1
# for i in range(1,n+1):
#     f = f * i
#     s = s + k*(1/(f)**i)
#     k = -k
# print(s)

# 90

# n = int(input())
# k = 1
# s = 0
# for i in range(3,n+1,2):
#     s = s + k*i
#     k = -k
# print(s)

# 93

n = int(input())
n = str(n)
b = []
for i in n:
    if int(i) % 2 != 0:
        b.append(i)
if len(b) == 0:
    print('Ededde tek reqem yoxdur')
else:
    print(min(b))