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
    
        
newbinaryheap = Heap(5)
# peakheap()
print(sizeofbinaryheap(newbinaryheap))