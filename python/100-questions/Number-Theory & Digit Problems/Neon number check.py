#Neon number check
#sum of digit of n**2  equals to n
n = int(input())

square = n**2
digit_sum = 0

for i in (str(square)):
    digit_sum += int(i)
    
if digit_sum == n:
    print("neon_number")
else:
    print("not neon number")