print "Hello World!"

def load_test_1(filename):
    f = open(filename)
    t = []
    line = f.readline()
    line = line.strip("\n")
    t.append(line)
    
    while line:
        line = f.readline()
        line = line.strip("\n")
        if line:
            t.append(line)
            
    return t

def load_test_2(filename):
    f = open(filename)
    test = []
    content = f.read()
    cont = content.split("\n")
    for element in cont:
        if element:
            test.append(int(element))
            
    return test

def cnt_sort(a):
    if len(a) == 1:
        return 0
    if len(a) > 1:
        mid = len(a)/2
        left = a[:mid]
        right = a[mid:]
        
        x = cnt_sort(left)
        y = cnt_sort(right)
        
        i = 0
        j = 0
        k = 0
        res = 0
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                a[k] = left[i]
                i = i+1
            elif left[i]>right[j]:
                a[k] = right[j]
                res = res + mid - i
                j = j+1
            k = k+1
            
        while i <len(left):
            a[k] = left[i]
            i = i+1
            k = k+1
            
        while j < len(right):
            a[k]= right[j]
            j = j+1
            k = k+1
            
    return res+x+y

# test cases provided in the discussion forum
A = [1,3,5,2,4,6]
B = [1,5,3,2,4]
C = [5,4,3,2,1]
D = [1,6,3,2,4,5]
E = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
F = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
G = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]

H = load_test_2("IntegerArray.txt")
cnt = cnt_sort(H)

print cnt
