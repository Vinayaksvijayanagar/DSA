#Replace all vowels with '*'

n = input()
s = n.lower()
for i in range(len(s)):
    if s[i] in "aeiou":
        s = s.replace(s[i],'*')
        

print(s)