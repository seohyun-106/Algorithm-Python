import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())

pic = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

rgb = 0
rb = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    visited[x][y] = True
    color = pic[x][y]

    for index in range(4):
        nx = x + dx[index]
        ny = y + dy[index]

        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and pic[nx][ny] == color:
                dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            rgb += 1

for i in range(N):
    for j in range(N):
        if pic[i][j] == 'G':
            pic[i][j] = 'R'

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            rb += 1

print(rgb, rb)
