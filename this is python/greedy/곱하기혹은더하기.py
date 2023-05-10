s = input()
arr = []

for i in range(len(s)):
    arr.append(int(s[i]))

answer = 0
for i in range(len(arr)):
    if answer <= 1 or arr[i] <= 1:
        answer += arr[i]
    else:
        answer *= arr[i]

print(answer)