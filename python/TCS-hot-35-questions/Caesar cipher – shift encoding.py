# Given a string and a shift value K, encode the string using Caesar cipher. Shift each letter forward by K 
# positions in the alphabet (wrap around z→a). Non-alphabetic characters remain unchanged.
# Sample input
# Hello World
# 3
# Sample output
# Khoor Zruog

s = input()
k = int(input())

st = ""

for ch in s:
    if ch.islower():
        st += chr((ord(ch) - ord('a')+k)%26 + ord('a'))
    elif ch.isupper():
        st += chr((ord(ch) - ord('A')+k)%26 + ord('A'))
    else:
        st += ch
        
print(st)