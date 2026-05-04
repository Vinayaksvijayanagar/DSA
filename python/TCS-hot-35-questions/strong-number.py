# A number is called a Strong number if the sum of the factorial of its digits equals the number
# itself. Given N, check if it is a Strong number.
# Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145

n = int(input())
temp = n
add = 0 


for i in  str(n):
    mul =1
    for j in range(1,int(i)+1):
        mul *= j
    add += mul
    
if temp == add:
    print("strong number")
else:
    exit()
        
        

