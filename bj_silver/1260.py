# import sys
# from collections import deque
# def dfs(start, visited):
#     visited[start] = True
#     print(start, end=" ")
#
#     for i in graph[start]:
#         if not visited[i]:
#             dfs(i, visited)
#
# def bfs(start, visited):
#     q = deque([start])
#     visited[start] = True
#
#     while q:
#         now = q.popleft()
#         print(now, end=" ")
#         for i in graph[now]:
#             if not visited[i]:
#                 visited[i] = True
#                 q.append(i)
#
# N, M, V = map(int, sys.stdin.readline().split())
#
# graph = [[] for _ in range(N+1)]
#
# dfs_visited = [False for _ in range(N+1)]
# bfs_visited = [False for _ in range(N+1)]
#
# for _ in range(M):
#     start, end = map(int, sys.stdin.readline().split())
#
#     graph[start].append(end)
#     graph[end].append(start)
#
# for i in graph:
#     i.sort()
#
# dfs(V, dfs_visited)
# print()
# bfs(V, bfs_visited)

from collections import deque
import sys
input = sys.stdin.readline

def dfs(now, dfs_visited):
    if not dfs_visited[now]:
        print(now, end=' ')
        dfs_visited[now] = True

        for next in graph[now]:
            dfs(next, dfs_visited)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

dfs_visited = [False for _ in range(N+1)]
dfs(V, dfs_visited)
print()

q = deque([V])
bfs_visited = [False for _ in range(N+1)]
while q:
    now = q.popleft()

    if not bfs_visited[now]:
        print(now, end=' ')
        bfs_visited[now] = True
        q.extend(graph[now])