n, m = map(int, input().split())

x, y, direction = map(int, input().split())

maps = list(list(map(int, input().split())) for _ in range(n))

dir = [0, 3, 2, 1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 1
checked = 0

idx = (dir.index(direction) + 1) % 4

while True:
    maps[x][y] = 1

    nx = x + dx[idx]
    ny = y + dy[idx]

    if maps[nx][ny] == 0:
        x = nx
        y = ny
        maps[nx][ny] = 1
        answer += 1

    if idx < 3:
        idx += 1
    else:
        idx = 0

    count = 0
    for line in maps:
        if 0 not in line:
            count += 1
    if count == n:
        break

print(answer)
