# Given a positive integer N, determine if it is prime. A prime number has exactly two factors: 
# 1 and itself. Print "Prime" or "Not Prime".
# Sample input
# 17
# Sample output
# Prime

n = int(input())
a = 2
for i in range(a,int((n**0.5)+1)):
    if n%i == 0:
        break
else:
    print("Prime")