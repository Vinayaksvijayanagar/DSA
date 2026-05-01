#reverse-word-order.py
n = input()
s = " "
a = n.split() 

for i in a[::-1]:
    s += i + " " 

print(s.strip())
    
