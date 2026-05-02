#find common elements in two list
a = list(map(int,input().split()))
b = list(map(int,input().split()))

print(sorted(set(a)) & sorted(set(b)))