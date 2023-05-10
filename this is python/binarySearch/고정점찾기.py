n = int(input())
numbers = list(map(int, input().split()))

start = 0
end = n - 1
answer = -1

while start <= end:
    mid = (start + end) // 2

    if numbers[mid] == mid:
        answer = mid
        break
    elif numbers[mid] > mid:
        end = mid - 1
    elif numbers[mid] < mid:
        start = mid + 1
    else:
        start += 1

print(answer)