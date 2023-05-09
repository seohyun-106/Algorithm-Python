s = input()

alphabets = []
numbers = []

for i in range(len(s)):
    if ord(s[i]) - ord('A') >= 0:
        alphabets.append(s[i])
    else:
        numbers.append(int(s[i]))

alphabets.sort()
number_sum = sum(numbers)

for a in alphabets:
    print(a, end="")

print(number_sum)

# K1KA5CB7
# AJKDLSI412K4JSJ9D