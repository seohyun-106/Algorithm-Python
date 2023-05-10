t = int(input())

for time in range(t):
    n, m = map(int, input().split())
    size = list(map(int, input().split()))
    board = [[] for _ in range(n)]

    for i in range(len(size)):
        board[i//m].append(size[i])

    d = [[0] * m for _ in range(n)]

    for i in range(n):
        d[i][0] = board[i][0]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                d[i][j] = board[i][j] + max(d[i][j-1], d[i+1][j-1])
            elif i == n-1:
                d[i][j] = board[i][j] + max(d[i-1][j-1], d[i][j-1])
            else:
                d[i][j] = board[i][j] + max(d[i-1][j-1], d[i][j-1], d[i+1][j-1])

    result = 0
    for i in range(n):
        result = max(result, d[i][m-1])
    print(result)
