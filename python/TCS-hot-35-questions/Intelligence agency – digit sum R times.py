    # An intelligence agency receives a number N and R. Sum all digits of N — repeat this R times. 
    # Each time, sum the digits of the result. Print the final single-digit result.
    # If R=0, print 0.
    # Sample input
    # 999
    # 3
    # Sample output
    # 9

N = int(input())
R = int(input())
output = 0

if R == 0:
    print(0)
else:

    for i in range(R):
        output = 0
        for j in str(N):
            output += int(j)
        N = output
            
print(output)