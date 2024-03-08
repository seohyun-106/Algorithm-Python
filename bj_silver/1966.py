from collections import deque

T = int(input())
for _ in range(T):
    answer = 0
    N, M = map(int, input().split())
    idx = deque([i for i in range(N)])
    importance = deque(list(map(int, input().split())))

    while idx:
        doc = idx.popleft()
        tmp = importance.popleft()

        m = max(importance) if importance else 0

        if tmp >= m:
            answer += 1
            if doc == M:
                print(answer)
                break
        else:
            idx.append(doc)
            importance.append(tmp)
