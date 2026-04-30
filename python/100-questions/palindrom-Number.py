#check the given  number palindrom or not
n = int(input())
m = n
rev = 0
while n>0:
    digit = n% 10
    rev = rev*10 + digit
    n = n//10
if m == rev:
    print("Palindrom")
else:
    print("not palindrom")