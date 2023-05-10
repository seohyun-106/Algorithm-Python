n = int(input())
arr = [[] for _ in range(n)]
for i in range(0, n):
    arr[i] = list(map(int, input().split()))
d = [[] for _ in range(n)]

d[0].append(arr[0][0])

for i in range(1, n):
    y = len(arr[i])
    for j in range(y):
        if j == 0:
            d[i].append(arr[i][j] + d[i-1][j])
        elif j == y-1:
            d[i].append(arr[i][j] + d[i-1][j-1])
        else:
            d[i].append(arr[i][j] + max(d[i-1][j-1], d[i-1][j]))

print(max(d[-1]))