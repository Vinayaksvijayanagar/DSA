# Find the missing number from 1..N
l = list(map(int,input().split()))
s = sum(l)
n = len(l)+1
m = (n*(n+1)//2) - s

print(m)