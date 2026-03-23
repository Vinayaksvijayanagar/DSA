from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1
        
def trverse(root):
    if not root:
        return None
    else:
        custom_queue = deque()
        custom_queue.append(root)
        while custom_queue:
            root_value = custom_queue.popleft(root)
            print(root_value)
            if root_value.leftchild is not None:
                custom_queue.append(root.leftchild)
            if root_value.rightchild is not None:
                custom_queue.append(custom_queue.rightchild)
                