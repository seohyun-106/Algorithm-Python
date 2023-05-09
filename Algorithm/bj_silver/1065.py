import sys

def isHansoo(n):
    cnt = 0
    for i in range(1, n + 1):
        if i <= 99:
            cnt += 1
        elif 100 <= i < 1000:
            a = i // 100
            b = (i % 100) // 10
            c = (i % 100) % 10
            if b == (a + c) / 2:
                cnt += 1
        else:
            continue
    return cnt


N = int(sys.stdin.readline())
print(isHansoo(N))
