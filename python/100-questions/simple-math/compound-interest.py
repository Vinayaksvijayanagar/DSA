p = int(input())
r = int(input())
t = int(input())

A = p * (1 + r/100) ** t
CI = A - p

print("Compound Interest =", CI)