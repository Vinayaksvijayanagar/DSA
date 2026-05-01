a = input()
b = input()
if sorted(a) == sorted(b):
    print("anagram")
else:
    print("not anagram")
    
#or 

a,b = input().split()
if sorted(a) == sorted(b):
    print("anagram")
else:
    print("not anagram")