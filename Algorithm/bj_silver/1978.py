import sys

N = int(input())
number = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in number:
    if i == 1:
        continue
    error = 0
    for j in range(2,i):
        if i % j == 0:
            error += 1
    if error == 0:
        answer += 1

print(answer)


