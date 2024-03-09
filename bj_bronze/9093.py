T = int(input())

for _ in range(T):
    str = input().split()
    answer = []

    for s in str:
        answer.append(s[::-1])

    print(' '.join(answer))