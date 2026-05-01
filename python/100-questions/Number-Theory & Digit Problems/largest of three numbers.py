# Find the largest of three numbersa
a,b,c = map(int,input().split(','))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
    
# use max
a,b,c = map(int,input().split())
print(max(a,b,c))
