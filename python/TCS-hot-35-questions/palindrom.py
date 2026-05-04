# Given a string or number, check if it reads the same forward and backward.
# For string: ignore case. Print "Palindrome" or "Not Palindrome".
# Sample input
# Madam
# Sample output
# Palindrome

n = input()
a = n.lower()

if a == a[::-1]:
    print("Palindrom")
