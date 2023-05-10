N, M = map(int, input().split())
s = []
# 1부터 N까지 자연수 중 중복 없이 M개를 고른다
# 고른 수열을 오름차순으로 출력
# 중복되는 수열은 출력하지 않는다 ex 3 4 == 4 3

# def permutation():
#     if len(s) == M:
#         print("len(s) == M")
#         s.sort()
#         print(s)
#         answer.append(s)
#         print("answer: ", answer)
#
#     for i in range(1, N+1):
#         if i in s:
#             continue
#         s.append(i)
#         permutation()
#         s.pop()
#
# permutation()

def dfs(start):
    if len(s) == M:
        print(" ".join(map(str, s)))
    for i in range(start, N+1):
        if i in s: continue
        s.append(i)
        dfs(i+1)
        s.pop()

dfs(1)