def dfs(idx, result):
    global add, sub, mul, div, min_value, max_value
    if idx == N:
       min_value = min(min_value, result)
       max_value = max(max_value, result)
    else:
        if add > 0:
            add -= 1
            dfs(idx+1, result + li[idx])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(idx+1, result - li[idx])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(idx+1, result * li[idx])
            mul += 1
        if div > 0:
            div -= 1
            dfs(idx+1, int(result/li[idx]))
            div += 1


N = int(input())
li = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

dfs(1, li[0])
print(max_value)
print(min_value)

