from collections import deque

n, m = map(int, input().split())
maze = list(list(map(int, input())) for _ in range(n))
visited = [[False] * m for _ in range(n)]

q = deque()
q.append((0, 0))

answer = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and maze[nx][ny] == 1:
                q.append((nx, ny))
                maze[nx][ny] += maze[x][y]

print(maze[n-1][m-1])
