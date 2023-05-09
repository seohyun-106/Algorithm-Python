import sys
sys.setrecursionlimit(10 ** 6)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    visited = [[False] * w for _ in range(h)]
    maps = []
    ground = []
    count = 0

    for i in range(h):
        maps.append(list(map(int, input().split())))
        for j in range(w):
            if maps[i][j] == 1:
                ground.append([i, j])

    def dfs(x, y):
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [1, 1, 1, 0, 0, -1, -1, -1]

        if not visited[x][y]:
            visited[x][y] = True

            for d in range(8):
                new_x = x + dx[d]
                new_y = y + dy[d]

                if 0 <= new_x < h and 0 <= new_y < w and maps[new_x][new_y] == 1:
                    dfs(new_x, new_y)


    for g in ground:
        if not visited[g[0]][g[1]]:
            count += 1
            dfs(g[0], g[1])

    print(count)
