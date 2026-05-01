#Count uppercase, lowercase, digits, specials
n = input()
l,u,d,special = 0,0,0,0
for i in n:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
    elif i.isdigit():
        d += 1
    else:
        special += 1

print(l,u,d,special)