from collections import deque

answer = 0

N = int(input())
pair = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]

q = deque([1])

while q:
    now = q.popleft()
    if not visited[now]:
        visited[now] = True
        answer += 1

    for i in graph[now]:
        if not visited[i]:
            q.append(i)

print(answer-1)
