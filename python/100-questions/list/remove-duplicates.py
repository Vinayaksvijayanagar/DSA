# Remove duplicates from a list (preserve order)
l = list(map(int,input().split()))
s = []
for i in l:
    if i not in s:
        s.append(i)
        
print(s)

