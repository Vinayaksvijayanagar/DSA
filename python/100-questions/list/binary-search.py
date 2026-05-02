# Binary search (sorted list)
n = list(map(int, input().split()))
target = int(input())

l = 0
h = len(n) - 1

while l <= h:
    mid = (l + h) // 2

    if n[mid] == target:
        print(f"Element {target} found at index {mid}")
        break
    elif n[mid] < target:
        l = mid + 1
    else:
        h = mid - 1
else:
    print("Not found")