# # 벡터 !
#
# import sys
#
# N = int(input())
#
# size = []
#
# for _ in range(N):
#     size.append(list(map(int, sys.stdin.readline().split())))
#
# result = [1] * N
#
# for i in range(N):
#     count = 0
#     for j in range(N):
#         if size[i][0] < size[j][0] and size[i][1] < size[j][1]:
#             count += 1
#     result[i] = count + 1
#
# print(" ".join(map(str, result)))

li = []

N = int(input())

for i in range(N):
    li.append(list(map(int, input().split())))

print(li)

result = [1] * N

for i in range(N - 1):
    for j in range(i + 1, N):
        if (li[i][0] - li[j][0]) * (li[i][1] - li[j][1]) > 0:
            smaller = i if li[i][0] < li[j][0] else j
            result[smaller] += 1

for n in result:
    print(n, end=' ')