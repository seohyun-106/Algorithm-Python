from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
labs = list(list(map(int, input().split())) for _ in range(n))

result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
safe = []
virus = []

def bfs():
    global result
    temp_virus = deque()
    for x, y in virus:
        temp_virus.append((x, y))
    while temp_virus:
        x, y = temp_virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                temp_virus.append((nx, ny))
    result = max(result, count())

def count():
    safe = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe += 1
    return safe

for i in range(n):
    for j in range(m):
        if labs[i][j] == 0:
            safe.append((i, j))
        elif labs[i][j] == 2:
            virus.append((i, j))

for comb in combinations(safe, 3):
    temp = copy.deepcopy(labs)
    for x, y in comb:
        temp[x][y] = 1
    bfs()

print(result)