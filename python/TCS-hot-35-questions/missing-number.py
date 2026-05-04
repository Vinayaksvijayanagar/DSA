# Given an array of N-1 integers containing distinct values from 1 to N (one number is missing), find the missing number.
n = list(map(int,input().split()))
l = len(n)+1

add = 0
for ch in n:
    add += ch
    
total = l*(l+1)//2
print(total-add)