# Given an array of stock prices for N days, find the maximum profit
# you can achieve by buying on one day and selling on a later day (single transaction only).
# If no profit possible, print 0.
# Sample input
# 6
# 7 1 5 3 6 4
# Sample output
# 5

n = int(input())
l = list(map(int, input().split()))

min_price = l[0]
max_profit = 0

for price in l:
    if price < min_price:
        min_price = price
    else:
        max_profit = max(max_profit, price - min_price)

print(max_profit)