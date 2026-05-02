#sort-list-check.py
l = list(map(int,input().split()))

if l == sorted(l):
    print("sorted")
else:
    print("not sorted")