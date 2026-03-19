from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
    def __str__(self):
        return str(self.data)
        
def insert(root,value):
    if root.data is None:
        root.data = value
    else:
        if value <= root.data:
            if root.leftchild is None:
                root.leftchild = Node(value)
            else:
                insert(root.leftchild,value)
        else:
            if root.rightchild is None:
                root.rightchild = Node(value)
            else:
                insert(root.rightchild,value)
                
def traverse(root):
    if not root:
        return None
    else:
        custom_queue = deque()
        custom_queue.append(root)
        while custom_queue:
            rootnode = custom_queue.popleft()
            print(rootnode.data)
            if rootnode.leftchild is not None:
                custom_queue.append(rootnode.leftchild)
            if rootnode.rightchild is not None:
                custom_queue.append(rootnode.rightchild)
                
def search(root,value):
    if  root.data == value:
        return "got buddy"
    else:
        if value <= root.data:
            if root.leftchild is not None and root.leftchild.data == value:
                return "got buddy in leftchild of root"
            else:
                return search(root.leftchild,value)
        else:
            if root.rightchild is not None and root.rightchild.data== value:
                return "got buddy in rightchild of root"
            else:
                return search(root.rightchild,value)
def getdeep(root):
    temp = root
    if temp is not None:
        temp = temp.rightchild
    return temp

# def delete(self,val)
root = Node(50)

insert(root, 30)
insert(root, 70)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 80)
traverse(root)
print(search(root,30))
print(getdeep(root))
