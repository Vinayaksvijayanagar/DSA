class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
    
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
        
    def push(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        
    def __str__(self):
        curr_node = self.top
        res = ''
        while curr_node is not None:
            res += str(curr_node.value)
            curr_node = curr_node.next
            if curr_node  is None:
                break
            res += "->\n"
        return res
    def pop(self):
        if self.top is None:
            return "stack is empty"
        else:
            popped_element = self.top
            self.top = self.top.next
            popped_element.next = None
            self.length -= 1
    def peak(self):
        return self.top
s = Stack()
s.push(1) 
s.push(2)  
s.push(3)       
print(s)
s.pop()
print(s)
print(s.peak())