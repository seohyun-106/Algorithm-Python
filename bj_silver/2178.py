from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
q = deque([(0, 0)])
visited[0][0] = True

while q:
    x, y = q.popleft()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = True

print(graph[N-1][M-1])