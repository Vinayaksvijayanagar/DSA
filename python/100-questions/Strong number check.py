#Strong number check
n = int(input())
s = 0
for i in (str(n)):
    f = 1
    for j in range(1,int(i)+1):
        f *= j
    s+=f

if s == n:
    print("strong")
else:
    print("not strong")
        

    