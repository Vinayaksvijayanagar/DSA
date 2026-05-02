n = int(input())

while n % 2 == 0 and n > 1:
    n = n // 2

if n == 1:
    print("Power of 2")
else:
    print("Not a power of 2")