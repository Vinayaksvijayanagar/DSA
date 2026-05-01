#Count even and odd numbers in a list
l = list(map(int,input().split()))
even = 0
for i in l:
    if i%2 == 0:
        even += 1
        
print(even,len(l)-even)