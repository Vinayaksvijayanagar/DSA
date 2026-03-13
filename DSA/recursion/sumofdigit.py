# def adddigit(n):
#     return sum([int(x) for x in str(n)])
# print(adddigit(23))

#another method
def adddigit(n):
   
    if n == 0:
        return n
    else:
        return n%10 + adddigit(n//10)
print(adddigit(23))
