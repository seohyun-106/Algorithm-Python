from collections import deque

n = int(input())
k = int(input())

board = [[0] * (n+1) for _ in range(n+1)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 2

l = int(input())
directions = dict()
route = deque()
route.append((1, 1))

for i in range(l):
    x, c = input().split()
    directions[int(x)] = c

x, y = 1, 1
board[x][y] = 1
time = 0
index = 0

def turn_direction(d, index):
    if d == 'D':
        return (index + 1) % 4
    else:
        return (index - 1) % 4

while True:
    time += 1
    nx = x + dx[index]
    ny = y + dy[index]

    if nx > n or nx < 1 or ny > n or ny < 1:
        break
    elif (nx, ny) in route:
        break
    else:
        if board[nx][ny] == 0:
            tx, ty = route.popleft()
            board[tx][ty] = 0
        board[nx][ny] = 1
        route.append((nx, ny))
        x, y = nx, ny
        if time in directions:
            index = turn_direction(directions[time], index)

print(time)