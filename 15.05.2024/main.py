# a = 'salam dünya'
# # a = list(a)
# a = a.split(' ')

# a = '_'.join(a)
# print(a)

# a= [1,2,3,4,4,4,5,6]
# a.insert(2,10)
# print(a)

# 77
# s = 0
# for i in range(1,100):
#     i=str(i)
#     s = s + i.count('3')
# print(s)

# 78
# n = int(input())
# k = []
# m = []
# for i in range(0,n):
#     a = int(input())
#     if a % 2 == 0:
#         m.append(a)
#     else:
#         k.append(a)
# print(m,k)

# # 79
# n=int(input())
# s=0
# while n%10==0:
#     s=s+1
#     n=n//10
# print(s)


# 80
# n=int(input())
# s=0
# if n>1:
#     for i in range(2,n//2+1):
#         if n%i==0:
#             s=s+1
#     if s>=1:
#         print("murekkeb ededdir")
#     else:
#         print("sade ededdir")
# else:
#     print('ne sadedir ne murekkeb')



# # 81
# n=int(input('n= '))
# s = 0
# k = 1
# for i in range(1,n+1):
#     s=s+k*i*(i+1)
#     print(s)
#     k= -k
# print(s)

# 82
# a=[3,4,15,9,18,16]
# s=0
# for i in a :
#     c = i**0.5
#     if c == int(c):
#         print(i)


# minimum yazılış
# a = [1,115,15,24,-5]
# min = a[0]
# for i in a:
#     if min>i:
#         min = i
# print(min)


#  2likden 16 liqa
# n=int(input())
# n = str(n)
# nl = len(n)-1
# onluq = 0
# for i in n:
#     onluq = onluq + int(i)*2**nl
#     nl = nl - 1
# reqemler ='0123456789ABCDEF'
# reqemler = list(reqemler)
# onaltiliq = ''
# while onluq >0 :
#     q = onluq%16
#     onaltiliq = reqemler[q] + onaltiliq
#     onluq = onluq//16
# print(onaltiliq)


# max ededi tapmaq defle

# def maxi(list):
#     max = list[0]
#     for i in list:
#         if i > max:
#             max = i
#     return max

# a = [30,2,3,4,5,6,7,21]
# result = maxi(a)
# print(result)

# reverse

# def reverse(list):
#     b = []
#     n = len(list)-1
#     while n >= 0:
#         c = list[n]
#         b.append(c)
#         n = n - 1
#     return b

# a = [11,12,24,25,30]
# print(reverse(a))

# count def


# def count(list,n):
#     say = 0
#     for i in list:
#         if i == n:
#             say = say + 1
#     return say
# a = [1,1,1,3,3,4,5,6,6,6]
# n = int(input())
# result = count(a,n)
# print(result)


# txt1 = 'zehra'
# print('tural','eli', 'nermin', sep=txt1+'-')
