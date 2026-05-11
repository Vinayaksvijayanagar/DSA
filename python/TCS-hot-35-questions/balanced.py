# Given a string containing only brackets '(', ')', '[', ']', '{', '}', 
# check if it is balanced. Print "Balanced" or "Not Balanced".
# Sample input
# {[()]}
# Sample output
# Balanced
s = input()
stack = []

for ch in s:
    if ch in "([{":
        stack.append(ch)
    elif ch == ')':
        if not stack or stack[-1] != '(':
            print("Not Balanced")
            break
        stack.pop()
    elif ch == ']':
        if not stack or stack[-1] != '[':
            print("Not Balanced")
            break
        stack.pop()
    elif ch == '}':
        if not stack or stack[-1] != '{':
            print("Not Balanced")
            break
        stack.pop()
else:
    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")
