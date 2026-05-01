#Automorphic number check
n = int(input())
digit = len(str(n))
m = n**2
o = m%(10**digit)
if n == o:
    print("auto")
else:
    print("not auto")