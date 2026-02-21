class Node:
    def __init__(self,data):
        self.data = data
        self.link = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def addend(self,data):
        new_node = Node(data)
        
        temp = self.head
        while temp.link != None:
            temp = temp.link
        temp.link = new_node
        
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end = '->')
            temp = temp.link
        print("None")
        
s1 = Linkedlist()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
s1.head = n1
n1.link = n2
n2.link = n3
s1.display()
s1.addend(5)
s1.display()