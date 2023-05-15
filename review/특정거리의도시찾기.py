from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance[x] = 0
q = deque()
q.append(x)

while q:
    now = q.popleft()
    length = len(graph[now])
    if length:
        for i in range(length):
            target = graph[now][i]
            if distance[now] + 1 < distance[target]:
                q.append(target)
                distance[target] = distance[now] + 1

check = False
for i in range(1, len(distance)):
    if distance[i] == k:
        print(i)
        check = True
if not check:
    print(-1)