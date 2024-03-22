from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(x, graph, visited):
    q = deque()
    visited[x] = True

    if graph[x]:
        q.extend(graph[x])

    while q:
        now = q.popleft()

        if not visited[now]:
            visited[now] = True
            q.extend(graph[now])

answer = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i, graph, visited)
        answer += 1

print(answer)