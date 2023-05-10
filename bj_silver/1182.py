def dfs(idx, sum):
    global count
    if idx == N:
        return
    sum += li[idx]
    if sum == S:
        count += 1
    dfs(idx+1, sum)
    dfs(idx+1, sum-li[idx])

N, S = map(int, input().split())
li = list(map(int, input().split()))

count = 0

dfs(0,0)
print(count)

from itertools import combinations
# for i in range(1, N+1):
#     c = list(combinations(li, i))
#     for j in c:
#         if sum(j) == S:
#             count += 1
#
# print(count)
