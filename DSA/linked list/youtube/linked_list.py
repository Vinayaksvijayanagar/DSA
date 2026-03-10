class Node:
    def __init__(self,data):
        self.data = data
        self.link = None
    
class Ll:
    def __init__(self):
        self.head = None
        
    def add_end(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.link != None:
            temp = temp.link
        temp.link = new_node
            
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end = '->')
            temp = temp.link
        print("None")
        
L1 = Ll()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
L1.head = n1
n1.link = n2
n2.link = n3
n3.link = None
n4 = Node(4)
L1.head = n4
n4.link = n1
n5 = Node(5)
n3.link = n5
n5.link = None
L1.display()
L1.add_end(6)
L1.display()   
        