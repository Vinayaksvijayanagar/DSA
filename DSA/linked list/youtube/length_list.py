class Node:
    def __init__(self,data):
        self.data = data
        self.link = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def count(self):
        count = 0 
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.link
        return count
        
    def display(self):
        temp = self.head
        while temp is not  None:
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
print("Length of linked list is:",s1.count())    