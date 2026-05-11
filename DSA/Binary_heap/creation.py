class Heap:
    def __init__(self,heapsize):
        self.heaplist = (heapsize+1)*[None]
        self.heapsize = 0
        self.maxheapsize = heapsize+1
        
def peakheap(heap):
    if not heap:
            return None 
    else:
            return heap.heaplist[1]
        
def sizeofbinaryheap(heap):
    if not heap:
        return None
    else:
        return heap.heapsize

def levelorderheap(heap):
    if not heap:
        return None
    else:
        for i in range(1,heap.heapsize+1):
            print(heap.heaplist[i])
        
newbinaryheap = Heap(5)
# peakheap()
print(sizeofbinaryheap(newbinaryheap))