# Given a sentence, print the words in reverse order (last word first). 
# Extra spaces between words should be ignored.

n = input()
res = ''
m = n.split()
m.reverse()

print(*m)

    
    