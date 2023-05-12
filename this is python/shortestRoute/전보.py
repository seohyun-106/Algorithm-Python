import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, city = map(int, input().split())
graph = [[] for _ in range(n+1)]
time = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

q = []
time[city] = 0
heapq.heappush(q, (time[city], city))

while q:
    t, now = heapq.heappop(q)
    if t < time[now]:
        continue
    for i in graph[now]:
        cost = t + i[1]
        if cost < time[i[0]]:
            time[i[0]] = cost
            heapq.heappush(q, (time[i[0]], i[0]))

answer = []

for i in range(1, n+1):
    if time[i] != INF and time[i] != 0:
        answer.append(time[i])

print(len(answer), max(answer))

# 3 2 1
# 1 2 4
# 1 3 2