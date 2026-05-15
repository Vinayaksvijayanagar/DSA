def selection_sort(l):
    for i in range(len(l)):
        min = i
        for j in range(i+1,len(l)):
            if l[j]<l[min]:
                min = j
        l[i], l[min] = l[min], l[i]
        
    return l
l = [2,1,3,4]
print(selection_sort(l))