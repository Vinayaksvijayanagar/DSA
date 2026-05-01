#Largest element in a list
l = list(map(int,input().split()))

max = 0
for i in l:
    if i > max:
        max = i
    else:
        continue
print(max)

# print(max(l))