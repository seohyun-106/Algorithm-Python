import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
tteok = list(map(int, sys.stdin.readline().rstrip().split()))


def cut_with(height):
    result = 0
    for i in tteok:
        if i >= height:
            result += i - height
    return result


start = 0
end = max(tteok)
height = 0

while start <= end:
    height = (start + end) // 2
    result = cut_with(height)

    if result == m:
        print(height)
        break
    elif result < m:
        end = height - 1
    elif result > m:
        start = height + 1
