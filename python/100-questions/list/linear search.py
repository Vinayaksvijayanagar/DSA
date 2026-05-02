# Linear search
l = list(map(int,input().split()))
target = int(input())
for i in l:
    if i == target:
        print(f"the element {i} is present")
        break
else:
    print("not present")