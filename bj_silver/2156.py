'''
dp -> 어떤 데이터를 저장할건지 생각해보자
n번째까지 마신 포도주의 최대 양!!

n = 1
dp[1] = arr[1]

n = 2
dp[2] = arr[1] + arr[2]

n = 3
i) O X O : dp[3] = arr[3] + arr[1] = arr[3] + dp[1]
ii) X O O : dp[3] = arr[3] + arr[2] + dp[0]
iii) O O X : dp[3] = dp[2]

n = n
i) O X O : dp[n] = arr[n] + dp[n-2]
ii) X O O : dp[n] = arr[n] + arr[n-1] + dp[n-3]
iii) O O X : dp[n] = dp[n-1]
이 세가지 경우 중에서 max 값을 찾으면
'''

import sys

n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(n)]

max_wine = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        max_wine[i] = wine[i]
    elif i == 1:
        max_wine[i] = wine[i-1] + wine[i]
    else:
        max_wine[i] = max(
            wine[i] + max_wine[i-2],
            wine[i] + wine[i-1] + max_wine[i-3],
            max_wine[i-1]
        )

print(max_wine[n-1])
