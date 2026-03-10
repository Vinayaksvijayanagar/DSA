class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)
    
class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
#append
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1
            
#__STR__   
    def __str__(self):
        curr_node = self.head
        res = ''
        while curr_node is not None:
            res += str(curr_node.value)
            curr_node = curr_node.next
            if curr_node is self.head:break
            res += "<->"
        return res
#add first
    def firstadd(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:    
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.length += 1    
        
# add last
    def addlast(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next  = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1

#traverse
    def traverse(self):
        temp_node = self.head
        if self.head is None:
            return None
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node is self.head:
                break
        return True   
#reverse
    def reverse(self):
        curr_node = self.tail
        if self.head is None:
            return None
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.prev
            if curr_node is self.tail:
                break
        return True   
#get
    def get(self,index):
        if index < -1 or index > self.length-1:
            return None
        elif index == 0:
            return self.head
        elif index == -1:
            return self.tail
        else:
            if index < self.length//2:
                curr_node = self.head
                for _ in range(index):
                    curr_node = curr_node.next
            else:
                curr_node = self.tail
                for _ in range (self.length-1,index,-1):
                    curr_node = curr_node.prev
        return curr_node
        
#set
    def set(self,index,value):
        if index < 0 or index > self.length-1:
            return None
        else :
            node = self.get(index)
            node.value = value
#search
    def search(self,target):
        temp_node = self.head
        index = 0
        while temp_node is not None:
            if temp_node.value == target:
                print("yes given element found ",index)
            temp_node = temp_node.next
            if temp_node is self.head :
                break
            index += 1
        print("not found")
#insert
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.firstadd(value)
        elif index == self.length :
            return self.addlast(value)
        else:
            new_node = Node(value)
            prev_node = self.get(index-1)
            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next.prev = new_node
            prev_node.next = new_node
        self.length += 1
#pop first
    def popfirst(self):
        if self.head is  None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_ele = self.head
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            popped_ele.next = None
            popped_ele.prev = None
        self.length -= 1
        return popped_ele
#pop last
    def poplast(self):
        if self.head is  None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            pop_ele = self.tail
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev= self.tail
            pop_ele.next = None
            pop_ele.prev = None
        self.length -= 1
#remove 
    def remove(self,index):
        if index < 0 or index > self.length-1:
           return False
        elif index == 0 :
            return self.popfirst()
        elif index == self.length-1:
            return self.poplast()
        else:
            pop_node = self.get(index)
            pop_node.next.prev = pop_node.prev
            pop_node.prev.next = pop_node.next   
            pop_node.next = None
            pop_node.prev = None 
l = CDLL()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
print(l)
l.firstadd(5)
print(l)
l.addlast(6)
print(l)
l.traverse()
l.reverse()

print(l.get(2))
l.set(2,99)
print(l)
l.search(36)
l.insert(1,88)
print(l)
l.popfirst()
print(l)
l.poplast()
print(l)
l.remove(2)
print(l)