#Second largest element
l = list(map(int,input().split()))
l1 = float('-inf')
l2 = float('-inf')
for i in l:
    if i > l1 :
        l2 = l1
        l1 = i
    elif i > l2 and i <l1:
        l2 = i
    else:
        pass
    
print(l2)
    