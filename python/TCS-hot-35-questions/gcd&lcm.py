# Given two positive integers A and B, compute and print their GCD (Greatest Common Divisor) and 
# LCM (Least Common Multiple) on separate lines.

a,b = map(int,input().split())

m =a 
n  = b

while b != 0:
    a,b = b,a%b
 
lcm = m*n//a   

    
print(a,lcm,sep='\n')