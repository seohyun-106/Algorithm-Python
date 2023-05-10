import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    rank = []
    for _ in range(N):
        rank.append(list(map(int, sys.stdin.readline().split())))

    rank.sort()
    top = rank[0][1]
    count = 1

    for i in range(1, N):
        if rank[i][1] < top:
            top = rank[i][1]
            count += 1

    print(count)