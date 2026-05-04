# Given an array of N integers, find the second largest distinct element. If no such element exists, print -1.
# Sample input
# 5
# 3 1 4 1 5
# Sample output
# 4
n = int(input())
m = list(map(int,input().split()))

if len(m)!= n:
    exit()
else:
    m.sort()
print(m[-2])