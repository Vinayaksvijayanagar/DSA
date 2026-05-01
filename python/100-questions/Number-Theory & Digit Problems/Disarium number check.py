#Sum of its digits powered by their positions = the number itself

n = int(input())
add = 0

for i,num in enumerate(str(n),1):
    add += (int(num))**(i)    
if add == n:
    print("disarium_number")
else:
    print("not disarium number")