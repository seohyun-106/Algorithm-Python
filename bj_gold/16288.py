import sys

N, K = map(int, sys.stdin.readline().split())
order = list(map(int, sys.stdin.readline().split()))

box = [0 for _ in range(K)]

line = False

for i in range(N):
    line = False
    for j in range(K):
        if order[i] > box[j]:
            box[j] = order[i]
            line = True
            break
    if not line:
        break

result = "YES" if line else "NO"
print(result)
