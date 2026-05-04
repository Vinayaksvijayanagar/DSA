# Given a number N, check if it is an Armstrong number. A number is Armstrong if the sum of its digits 
# each raised to the power of the number of digits equals N itself.
# Example: 153 = 1^3 + 5^3 + 3^3 = 1+125+27 = 153 ✓
# Sample input
# 153
# Sample output
# Armstrong

n = int(input())
l = len(str(n))
output = 0

for ch in str(n):
    output += int(ch)**l

if output == n:
    print("Armstrong")
    
else:
    print("not Armstrong")
    