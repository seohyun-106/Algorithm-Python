import sys

N = int(input())
number_list = list(map(int, list(sys.stdin.readline() for _ in range (N))))
number_list.sort()

for i in number_list:
    print(i)
