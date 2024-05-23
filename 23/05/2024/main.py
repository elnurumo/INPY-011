# 16
# n = int(input())
# s = 0
# while n != 0:
#     if n > 0 :
#         s = s + 1
#     n = int(input())
# print(s,'sayde musbet eded daxil ediniz')

# ededin reqemlerinin artan sirayla duzulmesin yoxla

# n = int(input())
# m = str(n)
# m = list(m)
# m.sort()
# m = ''.join(m)
# m = int(m)
# if n == m:
#     print('Yes')
# else:
#     print('No')

# 18

# n = int(input())
# n = str(n)
# f = 0
# for i in n:
#     if int(i) > 1:
#         f = 1
# if f == 1:
#     print('No')
# else:
#     print('Yes')

# ƏBOB

# a = int(input())
# b = int(input())
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(a)

# ƏKOB

# a = int(input())
# b = int(input())
# c = a*b
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(c/a)


# n = int(input())
# reqemler = '0123456789AB'
# s = ''
# while n>0:
#     q = n % 12
#     s = reqemler[q] + s
#     n = n // 12
# print(s)

# a = [3,4,7,9,60]
# b = []
# b.append(a[0])
# for i in range(1,len(a)):
#     c = a[i] - a[i-1]
#     b.append(c)
# print(b)

# n = int(input())
# b = []
# s = 0
# for i in range(0,n):
#     a = int(input())
#     b.append(a)
# for i in range(1,len(b)):
#     if i % 2 == 0:
#         s = s + b[i]**2
#     else:
#         s = s + b[i]
# print(s)

