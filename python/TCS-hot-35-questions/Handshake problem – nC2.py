# Before COVID-19, a meeting happened in Wuhan. Every person shook hands with every other person exactly once. 
# Given T test cases each with N people, print the total number of handshakes for each case.
# Constraints: 1<=T<=1000, 0
        
# Sample input
# 2
# 1
# 2

# Sample output
# 0
# 1
T = int(input())
f = []
for _ in range(T):
    N = int(input())
    f.append(N * (N - 1)// 2)
print(*f,sep="\n")