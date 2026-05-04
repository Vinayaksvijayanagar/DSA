# A class teacher distributes N books to N students. 
# She wants to exchange books so every student gets a DIFFERENT book than they currently have. 
# Find the number of valid exchanges (derangements).n!/e here e value is 2.718
# Answer modulo 100000007.
# If N=4: answer is 9.
# Sample input
# 4
# Sample output
# 9

# n  = int(input())
# fact = 1
# if n == 0:
#     print(1)
# else:
#     for i in range(1,n+1):
#         fact *= i
# p = fact/2.718
# print(round(p))

n = int(input())
mod = 100000007

if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    d1 = 0   # !1
    d2 = 1   # !2

    for i in range(3, n + 1):
        d = (i - 1) * (d1 + d2) % mod
        d1 = d2
        d2 = d

    print(d2)