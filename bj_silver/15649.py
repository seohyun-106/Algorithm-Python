N, M = map(int, input().split())
s = []

def permutation():
    if len(s) == M:
        print(' '.join((map(str, s))))
    for i in range(1, N+1):
        if i in s:
           continue
        s.append(i)
        permutation()
        s.pop()

permutation()