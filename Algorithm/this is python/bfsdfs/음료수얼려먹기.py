n, m = map(int, input().split())

tray = list(list(map(int, input())) for _ in range(n))

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    tray[x][y] = 1

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < n and 0 <= ny < m:
            if tray[nx][ny] == 0:
                dfs(nx, ny)


answer = 0
for i in range(n):
    for j in range(m):
        if tray[i][j] == 0:
            dfs(i, j)
            answer += 1

print(answer)