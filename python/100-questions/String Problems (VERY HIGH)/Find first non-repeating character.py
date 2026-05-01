#Find first non-repeating character
n = input()
d = {}
for i in n:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
        
for i in n:
    if d[i] == 1:
        print(i)
        break
else:
    print("none")