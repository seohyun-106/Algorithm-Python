import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    board = [[] for _ in range(n)]
    gold = list(map(int, input().split()))
    for i in range(n):
        board[i] = gold[i*m:i*m+m]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = board[i-1][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = board[i+1][j-1]

            left = board[i][j-1]

            board[i][j] += max(left_up, left, left_down)

    answer = 0
    for i in range(n):
        if board[i][m-1] > answer:
            answer = board[i][m-1]
    print(answer)

# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2