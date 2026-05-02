# A supermarket prints a code N on each product. The price of the item is the product (multiplication)
# of all the digits in N. Design software so that when the scanner reads N, it computes and prints the
# product of all digits.

# Sample input
# 234
# Sample output
# 24

n = int(input())
p = 1

for i in str(n):
    p*= int(i)
    
print(p)
    