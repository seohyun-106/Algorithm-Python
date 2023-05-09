from collections import deque

M, N = map(int, input().split())

tomato = []
total = 0
queue = deque()

for i in range(N):
    tomato.append(list(map(int, input().split())))
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])
        elif tomato[i][j] == -1:
            total += 1


def bfs():
    global total
    day = 0

    while queue:
        total += len(queue)

        if total == N*M:
            print(day)
            break

        for _ in range(len(queue)):
            curr_x, curr_y = queue.popleft()
            dx = [0, 0, -1, 1]
            dy = [1, -1, 0, 0]

            for k in range(4):
                new_x = curr_x + dx[k]
                new_y = curr_y + dy[k]

                if 0 <= new_x < N and 0 <= new_y < M:
                    if tomato[new_x][new_y] == 0:
                        tomato[new_x][new_y] = 1
                        queue.append([new_x, new_y])
        day += 1

    if total != N * M:
        print(-1)


bfs()
