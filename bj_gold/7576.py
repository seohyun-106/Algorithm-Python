import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

day = 0

tomato = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append((i, j))

while tomato:
    new = []
    while tomato:
        x, y = tomato.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if box[nx][ny] == 0:
                    box[nx][ny] = 1
                    new.append((nx, ny))

    tomato = deque(new)

    if new:
        day += 1

all = True
for i in range(N):
    for j in range(M):
        if not box[i][j]:
            all = False
            break

if all:
    print(day)
else:
    print(-1)