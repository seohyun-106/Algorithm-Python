K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    count = 0

    for line in lan:
        count += line // mid

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)