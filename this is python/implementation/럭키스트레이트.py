n = input()
mid = len(n) // 2

left = n[:mid]
right = n[mid:]

left_sum = 0
right_sum = 0
for i in range(mid):
    left_sum += int(left[i])
    right_sum += int(right[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
