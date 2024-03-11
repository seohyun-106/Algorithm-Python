# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# trees = list(map(int, sys.stdin.readline().split()))
#
# start = 0
# end = max(trees)
#
# while start <= end:
#     mid = (start + end) // 2
#
#     length = 0
#     for tree in trees:
#         if tree > mid:
#             length += tree - mid
#
#     if length >= m:
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(end)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2

    cut = 0
    for t in trees:
        if t > mid:
            cut += t - mid

    if cut < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)