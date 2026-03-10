class Node:
    def __init__(self,data):
        self.data = data
        self.link = None
        
class Llist:
    def __init__(self):
        self.head = None
        
    def deleteend(self):
        temp = self.head
        while temp.link.link is not None:
           temp = temp.link
        temp.link = None
        
    def display(self):
      
            temp = self.head
            while temp is not  None:
                print(temp.data,end = '->')
                temp = temp.link
            print("None")
    
s1 = Llist()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
s1.head = n1
n1.link = n2
n2.link = n3   
   
s1.display()
s1.deleteend()
s1.display()