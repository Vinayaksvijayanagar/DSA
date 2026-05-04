# Given two strings A and B, check if they are anagrams of each other 
# (contain the same characters with the same frequency, ignoring case). 
# Print "Anagram" or "Not Anagram". 
a = input().strip()
b = input().strip()

if sorted(a)==sorted(b):
    print("Anagram")
else:
    print("Not Anagram")