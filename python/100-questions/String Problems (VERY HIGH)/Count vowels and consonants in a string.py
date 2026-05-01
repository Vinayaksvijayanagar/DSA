#Count vowels and consonants in a string

s = input().lower()
vowels = 0
consonants = 0
for i in s:
     if i in "aeiou":
         vowels += 1
     else:
         consonants += 1
         
print(f"total vowels{vowels} and consonants {consonants}")