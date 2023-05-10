n = int(input())
requests = list(map(int, input().split()))
budget = int(input())

limit = 0

start = 0
end = max(requests)

while start <= end:
    mid = (start + end) // 2

    result = 0
    for request in requests:
        if request <= mid:
            result += request
        else:
            result += mid

    if result <= budget:
        start = mid + 1
    else:
        end = mid - 1

print(end)
