# bubble sort compare adjcnt elements and swap them acrdg

l = list(map(int,input().split()))
n = len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]      
print(l)