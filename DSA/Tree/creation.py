class Node:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        
    def __str__(self):
        return str(self.data)
    
new_t = Node("Drinks")
print(new_t)