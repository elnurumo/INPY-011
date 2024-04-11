# boolean: True, False
# if elif else

a = 24

if a >10:
    print("1")
    if a > 1:
        print("2")
else:
    print("3")
if a < 1:
    print("salam")
else:
    print("3")
if a<100:
    print("2")
else :
    print("3")

a = "salam"
print(a.upper())

b = [5,6,7,8,9,4,3,2,1]

def min_num(b):
    min_numb = b[0]
    for i in b:
        if i < min_numb:
            min_numb = i
    return min_numb

c = min_num(b)
print(c)

# 61, 67, 68, 63

#  61
saaat1 = int(input("Saat1: "))
deqiqe1 = int(input("Deqiqe1: "))
saniye1 = int(input("saniye1: "))
saaat2 = int(input("Saat2: "))
deqiqe2 = int(input("Deqiqe2: "))
saniye2 = int(input("Saniye2: "))
s1= saaat1*3600 + deqiqe1*60 + saniye1
s2 = saaat2*3600 +deqiqe2*60 +saniye2
print(s2 - s1)

# 63

n = input() 
m = len(n)
if m%2 == 0:
    print("0")
else:
    print(n[m//2])


# kitab
# 012
#  n[2]

# 67

n = int(input("n: "))
b = int(input("b: "))
s = 0
for i in range(1,n):
    if i**2 % b == 0:
        # s = s +1
        s += 1
print('ədədlərin sayı',s)

# 68
n = int(input()) # 3756
s = 0
c = 0
while n > 0:
    a = n % 10
    if a % 2 != 0:
        s = s + 1
        c = c + a
    n = n // 10
print(c,s)

# 66

n = int(input()) #2564
n = str(n)
for i in n:
    print(i)



# 67
# 1-ci method

n = int(input()) # 2354
n = str(n)
a = int(n[1])
b = int(n[2])
if b%2 != 0:
    print(a*b)
else: 
    print(a+b)

# 2-ci method

n=int(input())
a=n//100%10
b=n%100//10
if b%2!=0:
    print(a*b)
else:
    print(a+b)

















