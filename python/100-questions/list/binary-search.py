# Binary search (sorted list)
n = list(map(int,input().split()))
target = int(input())
l = 0 
h = len(n)
mid = l+h//2

if mid<target:
    l = mid+1
    h = len(n)
    for i in range(h):
        if n[i] == target:
            print(f"The element {n[i]} found")
            break
    else:
        print("not found")
else:
    l = o 
    h = mid-1
    for i in range(h):
        if n[i] == target:
            print(f"The element {n[i]} found")
            break
    else:
        print("not found")