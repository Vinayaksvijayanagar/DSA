# A chocolate factory packs chocolates into packets represented as an array of N integers. Empty 
# packets are represented as 0. Push all empty packets (0s) to the end of the conveyor belt while 
# keeping the order of non-zero packets.

# Sample input                               Sample output
# 8                                         4 5 1 9 5 0 0 0
# 4
# 5
# 0
# 1
# 9
# 0
# 5
# 0
n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

result = []
for i in arr:
     if i>0:
         result.append(i)
zeros = arr.count(0)
result.extend([0]*zeros)
print(*result)


               