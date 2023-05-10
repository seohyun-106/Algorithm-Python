n, m = map(int, input().split())
money = list(int(input()) for _ in range(n))
d = [10001] * (m+1)
d[0] = 0

for i in range(n):
    now_money = money[i]
    for j in range(now_money, m+1):
        d[j] = min(d[j], d[j-now_money] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
