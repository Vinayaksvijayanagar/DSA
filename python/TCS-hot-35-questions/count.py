# Given a string, count the number of vowels and consonants separately. 
# Ignore spaces and special characters. Print vowels count and consonants count.
# Sample input
# Hello World
# Sample output
# Vowels: 3
# Consonants: 7

n = input()
vowels = 0
consonants = 0

for ch in n.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
    else:
        pass
print(f"vowels : {vowels}")
print(f"consonants : {consonants}")