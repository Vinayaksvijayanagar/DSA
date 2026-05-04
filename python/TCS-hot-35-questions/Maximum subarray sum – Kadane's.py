# Given an array of integers (may include negatives), find the contiguous subarray 
# with the maximum sum and print that sum.
# Sample input
# 6
# -2 1 -3 4 -1 2
# Sample output
# 5

n = int(input())
l = list(map(int,input().split()))
max_arr = float("-inf")

for ch in range(n):
    add = 0
    for j in range(ch,n):
        add += l[j]
        max_arr = max(max_arr,add)
    
print(max_arr)

