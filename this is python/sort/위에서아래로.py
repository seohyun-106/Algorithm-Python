n = int(input())
array = list(int(input()) for _ in range(n))

array.sort(reverse=True)

for i in array:
    print(i, end=" ")
