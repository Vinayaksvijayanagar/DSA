#A number that is divisible by the sum of its digits

n = int(input())

digit_sum = 0
for num in (str(n)):
    digit_sum += int(num)
    
if n/digit_sum == 0:
    print("niven_number")
else:
    print("niven number")