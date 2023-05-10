N, K = map(int, input().split())
value = []
for _ in range(N):
    value.append(int(input()))

count = 0

for coin in reversed(value):
    if K == 0: break

    result = K // coin
    if result == 0:
        continue
    count += result
    K -= result * coin

print(count)