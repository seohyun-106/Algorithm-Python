import sys

def dfs(depth, idx):
    global min_difference
    if depth == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(i, N):
                if visited[i] and visited[j]:
                    start += ability[i][j] + ability[j][i]
                elif not visited[i] and not visited[j]:
                    link += ability[i][j] + ability[j][i]
        min_difference = min(min_difference, abs(start-link))

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

N = int(input())
ability = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False for _ in range(N)]
min_difference = 100

dfs(0, 0)
print(min_difference)




