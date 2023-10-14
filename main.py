# 1
# a = int(input("Введите число: "))
# k = 0
# for i in range(2, a // 2+1):
#     if (a % i == 0):
#         k = k+1
# if (k <= 0):
#     print("Число простое")
# else:
#     print("Число не является простым")


# 2
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))
# if a > c:
#     a = a + c
#     c = a - c
#     a = a - c
# if a > b:
#     a = a + b
#     b = a - b
#     a = a - b
# if b > c:
#     b = b + c
#     c = b - c
#     b = b - c
# print (a, "<", b, "<", c)


# 3
# import sys
#
# print("Enter massive: "),
#
# myList = map(int, sys.stdin.readline().split())
#
# max = myList[0]
# for e in myList[1:]:
#     if max < e:
#         max = e
#
# print
# "Max is " + str(max) + "\n"


# 4
# x = int(input())
#
# def fibonacci(n):
#     if n in (1, 2):
#        return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(x))


# 5
s = ['привет', 'привет', 'привет', 'привет', 'пока', 'досвидание', 'прощай', 'здарова', 'довстречи']
di = {}
for word in s:
    if word in di.keys():
        di[word] += 1
    else:
        di[word] = 1
key = max(di, key=di.get)
print(key, di[key])