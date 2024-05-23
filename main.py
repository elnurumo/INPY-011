# Klaviaturadan daxil edilmiş 2-dən böyük tam ədədin sadə vururqlarının alt-alta çapı

# n = int(input())
# s_vuruq = 2

# while n>1:
#     if n % s_vuruq ==0:
#         print(s_vuruq)
#         n = n//s_vuruq
#     else:
#         s_vuruq = s_vuruq + 1







# Klaviaturadan daxil edilmiş 2-dən böyük tam ədədin sadə bölənlərinin alt-alta çapı

# n = int(input())
# s_vuruq = 2
# b = []
# while n>1:
#     if n % s_vuruq ==0:
#         b.append(s_vuruq)
#         if b.count(s_vuruq) == 1:
#             print(s_vuruq)
#         n = n//s_vuruq
#     else:
#         s_vuruq = s_vuruq + 1

# Fibonacci ardıcıllığı hesablayan alqoritmi yazın. 
# Bu alqoritmin neçən-ci Fibonacci ədədini hesabladığınızı izah edin.

# def fiboncci(n):
#     a, b = 0, 1
#     for i in range(n): 
#         a, b = b, a+b
#     return b
# n = int(input())
# result = fiboncci(n)
# print(result)

# # 'Elnur'.upper()
# str()


# Verilmiş bir sıra üzrə ən kiçik ədədi tapmaq üçün bir proqram yazın. 
# proqramınız hansı metodlardan istifadə etdiyini izah edin.

# def min_num(list):
#     min_numb = list[0]
#     for i in range(1,len(list)):
#         if min_numb > list[i]:
#             min_numb = list[i]
#     return min_numb

# a = [12,18,24,30,4]




# Bir sətir veriləndə, sətirdəki hər bir simvolların sayını tapan bir 
# proqram yazın. Məsələn, "hello" sözünün daxilində hər bir hərfin neçə dəfə 
# işləndiyini tapan alqoritmi yazmalısınız.

# Bir listdə olan cüt ədədlərin cəmini hesablayan proqram yazın. 

# *
# **
# ***
# ****
# ***** terminalda, çıxışda bunu qaytarsın

# for i in range(1,6):
#     print(i*'*')


# list() vs split()
# a = 'Elnur, Ülvi, Tural, Nərmin'
# a = list(a) bütün simvolları ayırdı hissə hissə.
# a = a.split(', ') göndərdiyim əmrə görə ayırdı.
# print(a)  


# 94

# # 80
# n = int(input())
# s = 0
# if n > 1 :
#     for i in range(2, n//2 + 1):
#         if n % i == 0:
#             s = s + 1
#     if s == 0:
#         print('Sadədir')
#     else:
#         print('Mürəkkəbdir')
# elif n == 1:
#     print('1 nə sadədir, nə də mürəkkəb.')

# 89

# n = int(input())
# s = 0
# f = 1
# k = -1
# for i in range(1, n+1):
#     f = f * i
#     s = s + k*1/(f)**i
#     k = -k
# print(s)

# #  90 

# n = int(input())
# s = 0
# k = 1
# for i in range(3, n+1,2):
#     s = s + k*i
#     k = -k
# print(s)


# # 93

# n= int(input()) #2245
# min_num = 9
# k = 0
# while n > 0:
#     a = n % 10
#     if a % 2 != 0 and min_num > a:
#         min_num = a
#         k = 1
#     n = n//10
# if k == 0:
#     print("Ədəddə tək rəqəm yoxdur.")
# else:
#     print(min_num)

# # 91
# s = 0
# for i in range(100,1000): # 123
#     a = i // 100    #1
#     b = i //10%10   #2
#     c = i % 10      #3
#     if a % 3 == 0 and b % 3 ==0 and c % 3 == 0:
#         s = s + 1
# print(s)

# 94

# 1 ci metod
# hex_num = input()
# digit_num = int(hex_num, base=16)
# print(digit_num)

# 10 luqdan 16 -lığa

# digit_num = int(input())
# hex_num = hex(digit_num)[2:].upper()
# print(hex_num)

# # 2 -ci metod
# a = 'abc13231'
# digit_num = 0
# for i in a:
#     if i.isalpha():
#         digit_num = 16* digit_num + ord(i) - ord('A') + 10



# f1 = 1
# f2 = 1
# n = int(input())
# i = 2
# while i<n:
#     s = f2 + f1
#     f1 = f2
#     f2 = s
#     i = i +1

# print(s)

# a = [12,19,15,45,67]
# b = a
# del a[2]
# b.append('salam')
# b = b + [10,15]
# a.remove(a[len(a)-1])
# print(a)
# print(b)

# n = input()
# s = 0
# for i in n:
#     if  'A' <= i <= 'Z':
#         s = s + 1
# print(s) 

