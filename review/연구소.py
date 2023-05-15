from itertools import combinations
from collections import deque
import copy
import sys

input = sys.stdin.readline


def spread_virus(new_board, q):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if new_board[nx][ny] == 0:
                    new_board[nx][ny] = 2
                    q.append((nx, ny))


def count_safe(after_virus):
    safe = 0
    for i in range(n):
        for j in range(m):
            if after_virus[i][j] == 0:
                safe += 1
    return safe


results = []

n, m = map(int, input().split())

board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

virus = []
empty = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            empty.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))

empty_combi = list(combinations(empty, 3))

for combi in empty_combi:
    new_board = copy.deepcopy(board)
    q = deque(virus)
    for i in range(3):
        x, y = combi[i]
        new_board[x][y] = 1
    spread_virus(new_board, q)
    results.append(count_safe(new_board))
print(max(results))
