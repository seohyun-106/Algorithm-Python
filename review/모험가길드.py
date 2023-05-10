n = int(input())
level = list(map(int, input().split()))
level.sort()

group = 0
now = []

for i in range(n):
    now.append(level[i])
    if level[i] == len(now):
        group += 1
        now = []

print(group)