n = int(input())
m = len(str(n))
digit_sum = 0
total_sum = 0

for i in (str(n)):
    digit_sum = digit_sum + int(i)**m
    
if n == digit_sum:
    print("armstorng")
else:
    print("not armstrong")



    