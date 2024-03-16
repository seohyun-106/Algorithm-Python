import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))
numbers = sorted(line)

result = 0
now = int(1e9)
d = defaultdict(int)

for n in numbers:
    if d[n]:
        continue

    if n > now:
        result += 1

    d[n] = result
    now = n

answer = []
for n in line:
    answer.append(d[n])

print(*answer)