# from collections import deque
#
# result = []
#
# T = int(input())
#
# for _ in range(T):
#     M, N, K = map(int, input().split())
#     cabbage = []
#     for _ in range(K):
#         x, y = map(int, input().split())
#         cabbage.append((x, y))
#     visited = [[False for _ in range(M)] for _ in range(N)]
#     maps = [[0 for _ in range(M)] for _ in range(N)]
#
#     answer = 0
#
#     for y, x in cabbage:
#         maps[x][y] = 1
#
#     q = deque()
#     for y, x in cabbage:
#         if not visited[x][y]:
#             q.append((x, y))
#
#             while q:
#                 x, y = q.popleft()
#                 if visited[x][y]:
#                     continue
#
#                 visited[x][y] = True
#
#                 dx = [-1, 1, 0, 0]
#                 dy = [0, 0, -1, 1]
#
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#
#                     if 0 <= nx < N and 0 <= ny < M:
#                         if not visited[nx][ny] and maps[nx][ny] == 1:
#                             q.append((nx, ny))
#
#             answer += 1
#
#     print(answer)

import sys
sys.setrecursionlimit(100000)
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1

    def dfs(x, y, graph):
        if graph[x][y]:
            graph[x][y] = 0

            if x-1 >= 0:
                dfs(x-1, y, graph)
            if x+1 < N:
                dfs(x+1, y, graph)
            if y-1 >= 0:
                dfs(x, y-1, graph)
            if y+1 < M:
                dfs(x, y+1, graph)

    answer = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                dfs(i, j, graph)
                answer += 1

    print(answer)