'''
가치의 합이 i원이 되는 경우의 수를 구하는걸 부분문제로 세분화
1 <= i <= k

1원 동전만 사용하는 경우
dp[1] = dp[2] = dp[3] ... = dp[10] = 1

1원, 2원 동전을 사용하는 경우
i) 2원을 포함시키지 않을 때때 -> dp[k]
ii) 2원을 포함할 때 -> dp[k-2]

w원짜리 동전을 추가할 때
dp[k] = dp[k] + dp[k-w]
'''

import sys

coin_number, final_value = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(coin_number)]
dp = [1] + [0 for _ in range(final_value)]

for i in coins:
    for j in range(i, final_value + 1):
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[final_value])