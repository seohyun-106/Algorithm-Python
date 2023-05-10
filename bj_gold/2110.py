n, c = map(int, input().split())
houses = list(int(input()) for _ in range(n))
houses.sort()

start, end = 1, houses[n-1] - houses[0]
result = 0

while start <= end:
    mid = (start + end) // 2

    now = houses[0]
    count = 1

    for house in houses:
        if house - now >= mid:
            count += 1
            now = house

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
