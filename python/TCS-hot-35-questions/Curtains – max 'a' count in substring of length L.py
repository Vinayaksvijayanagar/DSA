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

max_count = 0

for i in range(0, len(s), l):
    sub = s[i:i+l]
    count_a = sub.count('a')
    max_count = max(max_count, count_a)

print(max_count)