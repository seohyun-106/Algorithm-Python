from collections import deque

N, K = map(int, input().split())

s = [i for i in range(1, N+1)]
q = deque(s)

answer = []

while q:
    for _ in range(K-1):
        tmp = q.popleft()
        q.append(tmp)

    answer.append(q.popleft())

print('<', ', '.join(map(str, answer)), '>', sep='')
