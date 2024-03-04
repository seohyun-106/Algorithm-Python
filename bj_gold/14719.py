H, W = map(int, input().split())
walls = list(map(int, input().split()))

answer = 0

for i in range(1, W-1):
    left_max = max(walls[:i])
    right_max = max(walls[i+1:])

    limit = min(left_max, right_max)

    if walls[i] < limit:
        answer += limit - walls[i]

print(answer)