'''
비용의 최소값

1번 집의 색 != 2번 집의 색
N번 집의 색 != N-1번 집의 색
i번의 집의 색 != i-1 / i != i+1

1번째 집: min(1.red, 1.green, 1.blue)

2번째 집:
dp[1] + 2.green
dp[2] + 2.blue

3번째 집:
dp[2] + 3.min


n번째 집:
red: arr[n][1] + min(arr[n-1][0] + arr[n-1][2]

'''

import sys
N = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

calculated_costs = [costs[0]] + [[0, 0, 0] for _ in range(N-1)]

for i in range(1, N):
    calculated_costs[i][0] = costs[i][0] + min(calculated_costs[i-1][1], calculated_costs[i-1][2])
    calculated_costs[i][1] = costs[i][1] + min(calculated_costs[i-1][0], calculated_costs[i-1][2])
    calculated_costs[i][2] = costs[i][2] + min(calculated_costs[i-1][0], calculated_costs[i-1][1])

print(min(calculated_costs[N-1]))