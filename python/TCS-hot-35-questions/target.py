# Given an array of integers and a target value T, 
# find and print the indices (0-based) of two numbers that add up to T. 
# Assume exactly one valid solution exists.
# Sample input
# 4
# 2 7 11 15
# 9
# Sample output
# 0 1

n = int(input())
l = list(map(int,input().split()))
target = int(input())

for i in range(n):
    for j in range(i+1,n):
        if l[i]+l[j] == target:
            print(i,j)
            break