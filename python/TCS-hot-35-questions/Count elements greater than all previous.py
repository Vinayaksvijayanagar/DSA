# Given an integer array of size N, find the count of elements whose value is greater than ALL of its prior elements.
# The 1st element is always counted.

# Example: [1,2,2,3] → count=3 (1,2,3 are each greater than all before them)
# Sample input
# 4
# 1 2 2 3
# Sample output
# 3

n  = int(input())
l = list(map(int,input().split()))
maxium = float("-inf")
cnt = 0

for i in range(len(l)):
    if l[i] > maxium:
        maxium = l[i]
        cnt += 1
    else:
        continue
print(cnt)  
