# Given an array of N integers, sort it in ascending order using Bubble Sort and print the sorted array. 
# The problem specifically asks for bubble sort implementation.
n = list(map(int,input().split()))
l = len(n)

for i in range(l):
    for j in range(l-i-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]= n[j+1],n[j]
            
print(*n)