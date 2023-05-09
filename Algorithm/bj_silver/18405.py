from collections import deque

maps = []
virus = []

N, K = map(int, input().split())

for i in range(N):
    maps.append(list(map(int, input().split())))
    for j in range(N):
        if maps[i][j] != 0:
            virus.append((maps[i][j], i, j))

S, X, Y = map(int, input().split())

virus.sort()
count = 0
q = deque(virus)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while q:
    if count == S:
        break

    for _ in range(len(q)):
        v, x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = v
                    q.append((maps[nx][ny], nx, ny))

    count += 1
print(maps[X-1][Y-1])