#72,73,

# def rafael(ders):
#     return ders
# x = 5
# print(x)

# 51
# x = 8
# s = 0
# anar = x+5
# amil = 2*x
# eltac = x
# s = anar + amil +eltac
# print(s/3)

# 61
# n = input()=
# reqemler = '0123456789'
# s = ''
# for i in n:
#     if reqemler.count(i) == 0:
#         s = s + i
# print(s)

# n = input()
# s = 0
# reqemler = '0123456789'
# for i in n:
#     if reqemler.count(i) == 1:
#         s = s + int(i)
# print(s)


# 72ci tap
# a=[2314,342,1206,4321,57,78965]
# s=0
# for i in range(0,len(a)):
#     a[i]=str(a[i])
#     s=int(min(a[i]))**2+int(max(a[i]))**2
#     a[i]=s
# print(a)

# 73
# a=[2345,421,356,876,45678,43321]
# s = 0
# for i in a:
#     i=str(i)
#     s= int(i[0])**2+int(i[-1])**2
#     print(s)



# a=[200,6,12,9,-6,-3,-90,1,5,3,0,40,-40]
# menfi=[]
# musbet=[]
# for i in a:
#     if i<0:
#         menfi.append(i)
#     elif i>0:
#         musbet.append(i)

# print('menfi ededi orta',sum(menfi)/len(menfi),'musbet ededi orta',sum(musbet)/len(musbet))


# 16 to 10

# n = input().upper()
# reqemler = '0123456789ABCDEF'
# reqemler = list(reqemler)
# nl = len(n) - 1
# s = 0
# for i in n:
#     s = s + reqemler.index(i) * 16**nl
#     nl = nl - 1
# print(s)


# 29

# n = int(input())
# n = str(n)
# s = 1
# for i in n:
#     if int(i) < 5:
#         s = s * int(i)
# print(s)


# 30 

# n = input()
# s = 0
# reqemler = '0123456789'
# reqemler = list(reqemler)
# for i in n:
#     if reqemler.count(i) == 1:
#         s = s + int(i)**2
# print(s)
     
