from collections import deque

def bfs(v):
    q = deque([v])

    while q:
        v = q.popleft()

        if v == K:
            return locations[v]

        for i in (v-1, v+1, v*2):
            if 0 <= i <= 100000 and not locations[i]:
                locations[i] = locations[v] + 1
                q.append(i)

N, K = map(int, input().split())
locations = [0 for _ in range(100001)]
print(bfs(N))

# sec = 0
# locations = [N]
#
# while True:
#     sec += 1
#
#     tmp = set()
#
#     for loc in locations:
#         tmp.add(loc - 1)
#         tmp.add(loc + 1)
#         tmp.add(loc * 2)
#
#     if K in tmp:
#         break
#     else:
#         locations = tmp
#
# print(sec)