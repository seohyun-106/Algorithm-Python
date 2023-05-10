n = int(input())
values = list(map(int, input().split()))

values.sort()

start, end = 0, n-1
answer = [values[start], values[end]]
minimum = abs(sum(answer))

while start < end:
    result = values[start] + values[end]

    if abs(result) < minimum:
        minimum = abs(result)
        answer = [values[start], values[end]]

    if result < 0:
        start += 1
    elif result > 0:
        end -= 1
    else:
        break

print(answer[0], answer[1])
