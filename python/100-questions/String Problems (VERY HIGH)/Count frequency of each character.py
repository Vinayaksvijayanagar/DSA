#Count frequency of each character
s = input()
d = {}
for i in s.strip():
    if i in d:
        d[i]+= 1
    else:
        d[i] = 1
print(d)