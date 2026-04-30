# GCD of two numbers(Euclidean algorithm (fast method) a,b = b,a%b)
a,b = map(int,input().split())
while b != 0 :
    a,b = b,a%b
    
print(a)