#Armstrong for N digits (generalised)
n = int(input())
for i in range(n+1):
    m = len(str(i))
    digit_sum = 0
    for j in (str(i)):
        digit_sum += int(j)**m
    if i == digit_sum:
        print(i , end=",")
        
        
        