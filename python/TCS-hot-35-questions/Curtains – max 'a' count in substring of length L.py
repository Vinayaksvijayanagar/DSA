# A furnishing company manufactures curtains. Given a string S (only 'a' and 'b') and an integer L, 
# divide S into substrings of length L. If the last part has fewer than L characters, it is still a valid substring.
# Find the maximum number of 'a's in any single substring.
# Sample input
# aababaa
# 3
# Sample output
# 3 
s = input()
l = int(input())

length = len(s)

if length%l == 0:
    print(length//l)

else:
    print((length//l)+1)