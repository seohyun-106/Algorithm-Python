def isLeapYear(x):
    if (x%4 == 0 and x%100 != 0):
        return 1
    elif (x%400 == 0):
        return 1
    else:
        return 0

year = int(input())
print(isLeapYear(year))
