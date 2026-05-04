# Given N, print the Nth Fibonacci number. The series starts: 0 1 1 2 3 5 8 13 21...
# So for N=1, output is 0. For N=7, output is 8.
# Sample input
# 7
# Sample output
# 8
n = int(input())

a = 0
b = 1
for i in range(n-1):
    a,b= b,a+b
    
print(a)