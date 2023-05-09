n, x = map(int, input().split())
a = list(map(int, input().split()))

start = 0
end = n-1

count = -1

while start < end:
    if a[start] == x and a[end] == x:
        count = end - start + 1
        break

    mid = (start + end) // 2
    if x < a[mid]:
        end = mid - 1
    elif x > a[mid]:
        start = mid + 1
    else:
        if x > a[start]:
            start += 1
        elif x < a[end]:
            end -= 1

print(count)
