N = int(input())

generator_flag = False

for i in range (1, N):
    i_number = list(map(int, list(str(i))))
    result = i + sum(i_number)
    if result == N:
        print(i)
        generator_flag = True
        break
    else: continue

if not generator_flag:
    print(0)