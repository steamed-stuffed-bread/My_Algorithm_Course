import numpy as np

print "Hello World!"

def load_test(filename):
    f = open(filename)
    test = []
    content = f.read()
    cont = content.split("\n")
    for element in cont:
        if element:
            test.append(int(element))
            
    return test

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a,b

def partition(a,l,h):
    i = l+1
    j = l+1
    pivot = a[l]
    
    while j < h+1:
        if a[j] <= pivot:
            a[i], a[j] = swap(a[i],a[j])
            i = i+1
        j = j+1
            
    return i-1

def three_midian(a,l,h):
    m = l+(h-l)//2
    val = [a[l],a[m],a[h]]
    mid = val[val.index(np.median(val))]
    return mid

def q_sort_helper(num, a,l,h):
    if l < h:
        if num == 2:
            a[l],a[h] = swap(a[l],a[h])
        elif num == 3:
            mid = a.index(three_midian(a,l,h))
            a[l],a[mid] = swap(a[l],a[mid])
            
        pivot = partition(a,l,h)
        
        a[l], a[pivot] = swap(a[l], a[pivot])
        
        left = q_sort_helper(num,a,l,pivot-1)
        right = q_sort_helper(num,a,pivot+1,h)
    else:
        return 0
    
    return h-l+left+right

def q_sort(num, D):
    return q_sort_helper(num, D, 0, len(D)-1)

if __name__=="__main__":
    D = load_test("QuickSort.txt")
    num = 1 # 1 2 3 -> first last three_median
    res = q_sort(num, D)
    print res