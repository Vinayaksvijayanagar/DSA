#Average of elements in a list
l = list(map(int,input().split()))

lenth = len(l)
sum = 0
for i in l:
    sum += i
print(f"{sum/lenth:.2f}")