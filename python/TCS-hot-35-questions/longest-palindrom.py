# Given a string S, find and print the longest palindromic substring.
# If multiple substrings of the same maximum length exist, print the first one.
# Sample input
# babad
# Sample output
# bab

s = input()
ans = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        if sub == sub[::-1]:
            if len(sub) > len(ans):
                ans = sub

print(ans)