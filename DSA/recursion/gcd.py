# def gcd(a,b):
#     rem = a%b
#     if rem == 0:
#         return b
#     else:
#         return (gcd(b,rem))

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(48,18))   