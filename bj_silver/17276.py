def rotate_in_clockwise(n, matrix):
    new = [[0 for _ in range(n)] for _ in range(n)]

    main_diagonal = []
    sub_diagonal = []
    col = []
    row = []
    for i in range(n):
        main_diagonal.append(matrix[i][i])
        sub_diagonal.append(matrix[n-1-i][i])
        col.append(matrix[i][n//2])
        row.append(matrix[n//2][i])

    for i in range(n):
        # 주대각선 -> 가운데열
        new[i][n//2] = main_diagonal[i]
        # 가운데열 -> 부대각선
        new[i][n-1-i] = col[i]
        # 부대각선 -> 가운대행
        new[n//2][i] = sub_diagonal[i]
        # 가운데행 -> 주대각선
        new[i][i] = row[i]

    for i in range(n):
        for j in range(n):
            if not new[i][j]:
                new[i][j] = matrix[i][j]

    return new


def rotate_in_counterclockwise(n, matrix):
    new = [[0 for _ in range(n)] for _ in range(n)]

    main_diagonal = []
    sub_diagonal = []
    col = []
    row = []
    for i in range(n):
        main_diagonal.append(matrix[i][i])
        sub_diagonal.append(matrix[i][n-1-i])
        col.append(matrix[i][n//2])
        row.append(matrix[n//2][i])

    for i in range(n):
        # 주대각선 -> 가운데행
        new[n//2][i] = main_diagonal[i]
        # 가운데열 -> 주대각선
        new[i][i] = col[i]
        # 부대각선 -> 가운데열
        new[i][n//2] = sub_diagonal[i]
        # 가운데행 -> 부대각선
        new[i][n-1-i] = row[n-1-i]

    for i in range(n):
        for j in range(n):
            if not new[i][j]:
                new[i][j] = matrix[i][j]

    return new

T = int(input())

for _ in range(T):
    n, d = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    if d < 0:
        for _ in range(abs(d) // 45):
            matrix = rotate_in_counterclockwise(n, matrix)
    else:
        for _ in range(d // 45):
            matrix = rotate_in_clockwise(n, matrix)

    for i in range(n):
        print(*matrix[i])