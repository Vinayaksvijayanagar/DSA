# Given an array of N integers containing only 0s, 1s, and 2s (representing risk severity), 
# sort the array. 0=low, 1=medium, 2=high risk. Output the sorted array.
# Sample input
# 6
# 0 2 1 2 0 1
# Sample output
# 0 0 1 1 2 2

n = int(input())
l = list(map(int,input().split()))
if len(l) != n:
    print("Invalid input")
    
zeros = 0 
ones = 0 
twos = 0

zeros = l.count(0)
ones = l.count(1)
twos = l.count(2)
p = [0]*zeros+[1]*ones+[2]*twos
print(*p)
