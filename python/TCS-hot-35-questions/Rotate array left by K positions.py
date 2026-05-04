# Given an array of N integers and a value K, left-rotate the array by K positions.
# After rotating, print the resulting array.
# Sample input
# 5
# 1 2 3 4 5
# 2
# Sample output
# 3 4 5 1 2
n = int(input())
l = list(map(int,input().split()))
k = int(input())
l1 = []
l2 = []
if len(l) != n:
    exit()
    
else:
    for i in range(0,k):
        l1.append(l[i])
        
    for j in range(k,len(l)):
        l2.append(l[j])
        
print(*(l2+l1))
