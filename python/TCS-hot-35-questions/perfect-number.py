# A perfect number equals the sum of its proper divisors (all divisors excluding the number itself). 
# Given N, print "Perfect" or "Not Perfect".
# Example: 6 = 1+2+3 = 6 ✓

n = int(input())
add = 0

for i in range(1,n):
    if n%i == 0:
        add += i
    
if add == n:
    print("perfect number")
else:
    print("not perfect")