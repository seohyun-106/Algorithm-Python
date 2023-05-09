import sys

n = int(sys.stdin.readline())
houses = list(map(int, input().split()))
houses.sort()

result = 100000
index = n // 2
answer = houses[index]

for index in range(index - 1, index + 2):
    antenna = houses[index]
    distance = 0
    for i in range(n):
        if houses[i] >= antenna:
            distance += houses[i] - antenna
        else:
            distance += antenna - houses[i]

    if distance < result:
        result = distance
        answer = antenna

print(answer)