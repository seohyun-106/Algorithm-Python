## 한줄로 입력받은거 순서대로 리스트 추가하기 -> for문 대신 map !!

n = int(input())
num_list = list(map(int, input().split()))

max = num_list[0]
min = num_list[0]

for i in num_list:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)