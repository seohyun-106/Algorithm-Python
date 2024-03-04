s = input()
a = s.count('a')

s += s[0:a-1]

answer = int(1e9)

for i in range(len(s) - (a-1)):
    answer = min(answer, s[i:i+a].count('b'))

print(answer)