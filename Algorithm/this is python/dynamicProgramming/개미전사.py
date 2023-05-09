n = int(input())
storage = list(map(int, input().split()))
d = [0] * n

d[0] = storage[0]
d[1] = max(storage[0], storage[1])
for i in range(2, n):
    yes = storage[i] + d[i-2]
    no = d[i-1]
    d[i] = max(yes, no)

print(d[n-1])