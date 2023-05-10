import sys

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    if i == 1:
        continue

    error = 0
    # 이게 왜 되는가 ?
    for j in range(2, i):
        if i % j == 0:
            error += 1

    if error == 0:
        print(i)