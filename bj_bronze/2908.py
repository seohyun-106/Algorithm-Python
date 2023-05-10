import sys

# def reverse_number(n):
#     new = 0
#     new_number = 0
#     for i in range(len(n)-1, -1, -1):
#         new += int(n[i]) * (10 ** i)
#     new_number += new
#     return new_number

a, b = sys.stdin.readline().split()

# 문자열 list로 만들고 역순으로
a = int(a[::-1])
b = int(b[::-1])

if a > b: print(a)
else: print(b)