#Print first N Fibonacci numbers

n = int(input())
a,b = 0,1
l =[]
for _ in range(n):
    l.append(str(a))
   
    a,b = b,a+b
print(','.join(l))