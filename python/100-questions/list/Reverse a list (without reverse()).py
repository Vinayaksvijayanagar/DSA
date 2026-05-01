#Reverse a list (without reverse())
l = list(map(int,input().split()))
s = l
a = 0
b = len(l)-1
while a<b:
    l[a],l[b] = l[b],l[a]
    a+=1
    b -= 1
    
print(l)