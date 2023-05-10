n = int(input())
k = int(input())

# 메모리 초과 풀이
# b = []
# for i in range(1, n + 1):
#     for j in range(1, n+1):
#         b.append(i * j)
# b.sort()
# mid = sum(b) // (n * n)
# print(b[k-1])

answer = 0
start, end = 1, n*n

while start <= end:
    mid = (start + end) // 2

    count = 0

    for i in range(1, n+1):
        count += min(mid // i, n)

    if count >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
