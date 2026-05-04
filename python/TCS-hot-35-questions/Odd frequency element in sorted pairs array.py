# Given an array where every element appears an even number of times except one element 
# (which appears an odd number of times), and equal elements appear in pairs. Find the odd-occurring element.
# Valid input: elements are in pairs, no 3 consecutive same elements.
# Sample input
# 5
# 2 2 3 1 1
# Sample output
# 3

n = int(input())
l = list(map(int, input().split()))

res = 0

for num in l:
    res ^= num

print(res)
            
        
