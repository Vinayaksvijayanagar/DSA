a,b = map(int,input().split(','))
m,n = a,b
while b!=0:
    a,b = b,a%b

lcm = (m*n)//a
print(lcm)
