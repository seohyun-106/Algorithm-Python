from collections import deque

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
# visited = [[False for _ in range(N)] for _ in range(N)]

def bfs(x, y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny]:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
                    count += 1

    return count

result = []

for i in range(N):
    for j in range(N):
        if graph[i][j]:
            result.append(bfs(i, j, graph))

result.sort()
print(len(result))
print(*result, sep='\n')