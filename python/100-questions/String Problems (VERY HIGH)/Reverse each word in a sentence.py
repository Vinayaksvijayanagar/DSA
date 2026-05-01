#Reverse each word in a sentence
n = input()

result = " "

for i in n.split():
    result += i[::-1] + " "
    
print(result)
    