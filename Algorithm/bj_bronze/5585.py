def calculate(money):
    global count, return_price
    count += return_price // money
    return_price %= money

price = int(input())

return_price = 1000 - price

count = 0

calculate(500)
calculate(100)
calculate(50)
calculate(10)
calculate(5)
calculate(1)

print(count)