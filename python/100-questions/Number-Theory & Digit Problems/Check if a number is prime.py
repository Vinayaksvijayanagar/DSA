#Check if a number is prime
n = int(input())
if n<2 :
    print("not prime")
else:
    for i in range(2,int((n**0.5+1))):
        if n%i == 0:
            print("not a prime")
            break
    else:
        print("prime")
        