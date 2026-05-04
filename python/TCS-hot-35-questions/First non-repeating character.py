# Given a string, find and print the first character that does not repeat
# (appears exactly once). If all characters repeat, print "None" or "-1".
# Sample input
# programming
# Sample output
# p
n = input()

for i in range(len(n)):
    count = 0 
    for j in range(i,len(n)):
        if n[i] == n[j]:
            count += 1
    if count == 1:
        print(n[i])
        break
else:
    print("None")
            