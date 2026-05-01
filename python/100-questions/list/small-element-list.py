#small-element-list
#Largest element in a list
l = list(map(int,input().split()))

min = float('inf')
for i in l:
    if i < min:
        min = i
    else:
        continue
print(min)

# print(min(l))