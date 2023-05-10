n = int(input())
values = list(map(int, input().split()))

values.sort()

group = []
count = 0

for i in range(n):
    if len(group) < values[i]:
        group.append(values[i])
        if len(group) == values[i]:
            count += 1
            group = []

print(count)