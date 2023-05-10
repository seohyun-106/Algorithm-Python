import sys

M, N = map(int, sys.stdin.readline().split())
needs = [int(sys.stdin.readline()) for _ in range(N)]

needs.sort()

lack = sum(needs) - M
anger = [0 for _ in range(N)]
result = 0

# 이게 왜 시간초과일까 ...

# for i in range(lack):
#     anger[i % N] += 1
#
# for i in anger:
#     result += i ** 2
#
# result %= 2 ** 64
# print(result % (2**64))

for i in range(N):
    tmp = min(needs[i], lack // (N-i))
    result += tmp ** 2
    lack -= tmp

result %= 2 ** 64
print(result)