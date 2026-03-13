def feb(n):
    assert n>=0 and int(n)==n,"enter positive number"
    if n == 1 or n == 0:
        return n
    else:
         return feb(n-1)+feb(n-2)
n = int(input("enter the number"))
print(feb(n))