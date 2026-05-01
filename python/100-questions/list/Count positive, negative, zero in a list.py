#Count positive, negative, zero in a list

l = list(map(int,input().split()))
pos = 0
neg = 0
zeros = 0
for i in l:
    if i<0:
        neg += 1
    elif i>0:
        pos += 1
    else:
        zeros += 1
        
print(pos,neg,zeros)