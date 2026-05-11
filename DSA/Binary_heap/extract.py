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
            
def adjust_insert(heap,index,type):
    parent = index//2
    if index<=1:
        return None
    if type == "min":
        if heap.heaplist[index] < heap.heaplist[parent]:
            temp = heap.heaplist[index]
            heap.heaplist[index] = heap.heaplist[parent]
            heap.heaplist[parent] = temp
        adjust_insert(heap,parent,type)
    elif type == "max":
        if heap.heaplist[index] > heap.heaplist[parent]:
            temp = heap.heaplist[index]
            heap.heaplist[index] = heap.heaplist[parent]
            heap.heaplist[parent] = temp
        adjust_insert(heap,parent,type)

def insert(heap,nodevalue,type):
    if heap.heapsize+1 == heap.maxheapsize:
        return "binary heap is full"
    heap.heaplist[heap.heapsize+1] = nodevalue
    heap.heapsize += 1
    adjust_insert(heap,heap.heapsize,type)
    
    return "inserted element to binary heap !! "

def adjust_extract(heap,index,type):
    leftchild_index= 2*index
    rightchild_index= (2*index)+1
    swaped_index = 0
    
    if index > heap.heapsize:
        return None
    #for one child
    elif heap.heapsize == leftchild_index:
        if type == "min":
            if heap.heaplist[index] > heap.heaplist[leftchild_index]:
                temp = heap.heaplist[index]
                heap.heaplist[index] = heap.heaplist[leftchild_index]
                heap.heaplist[leftchild_index] = temp
            return
        else:
            if heap.heaplist[index] < heap.heaplist[leftchild_index]:
                temp = heap.heaplist[index]
                heap.heaplist[index] = heap.heaplist[leftchild_index]
                heap.heaplist[leftchild_index] = temp
            return
    #if we have two children 
    else:
        if type == "min":
            if heap.heaplist[leftchild_index]<heap.heaplist[rightchild_index]:
                swaped_index = leftchild_index
            else:
                swaped_index  = rightchild_index
            if heap.heaplist[index] > heap.heaplist[swaped_index]:
                temp = heap.heaplist[index]
                heap.heaplist[index] = heap.heaplist[swaped_index]
                heap.heaplist[swaped_index] = temp
                
        else:
            if heap.heaplist[leftchild_index]>heap.heaplist[rightchild_index]:
                swaped_index = leftchild_index
            else:
                swaped_index  = rightchild_index
            if heap.heaplist[index] < heap.heaplist[swaped_index]:
                temp = heap.heaplist[index]
                heap.heaplist[index] = heap.heaplist[swaped_index]
                heap.heaplist[swaped_index] = temp
        adjust_extract(heap,swaped_index,type)

def extract(heap,type):
        if heap.heapsize == 0:
            return "empty heap"
        else:
            extracted = heap.heaplist[1]
            heap.heaplist[1] = heap.heaplist[heap.heapsize]
            heap.heaplist[heap.heapsize] = None
            heap.heapsize -= 1
            adjust_extract(heap,1,type)
            return extracted
new_heap = Heap(5)
insert(new_heap,2,"min")
insert(new_heap,4,"min")
insert(new_heap,1,"min")
insert(new_heap,-1,"min")
insert(new_heap,5,"min")
levelorderheap(new_heap)
extract(new_heap,"min")
levelorderheap(new_heap)