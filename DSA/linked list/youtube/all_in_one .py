class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
        #Additaion 
    def add(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        
          
        
    # delete
    def sub(self):
        temp = self.head
        while temp.next.next is not  None:
            temp = temp.next
        temp.next = None
        
    #count
    def count(self):
        count = 0 
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    #Display
    def display(self):
        temp = self.head
        while (temp is not None):
            print(temp.data,end = "->")
            temp = temp.next
        print("None")
L1 = Linkedlist()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
L1.head = n1
n1.next = n2
n2.next= n3
n3.next = None
          
    
L1.display()       
L1.add(4)
L1.display() 
L1.sub()
L1.display()
print(L1.count())