print "Hello World!"
import numpy as np
import copy

def readfile(filename):
    G = []
    f = open(filename)
    (ks, ni) = [int(x) for x in f.readline().split()]
    for line in f.readlines():
        (v,w) = [int(x) for x in line.split()]
        G.append((v,w))
    return ks, ni, G

def kga(cap, size, G):
    A = np.zeros((size+1, cap+1), dtype=int)
    for i, item in enumerate(G):
        v = item[0]
        w = item[1]
        for j in range(cap+1):
            not_added = A[i][j]
            if w <= j:
                added = A[i][j-w] + v
            else:
                added = 0
            A[i+1][j] = max(added, not_added)
    return A[size][cap]

def big_kga(cap, size, G):
    good = np.zeros(cap+1, dtype=int)
    temp = np.zeros(cap+1, dtype=int)
    for i,item in enumerate(G):
        v = item[0]
        w = item[1]
        temp[:w] = good[:w]
        for j in range(w,cap+1):
            added = good[j]
            not_added = good[j-w] + v
            if not_added > added:
                temp[j] = not_added
        good = copy.copy(temp)
        if i % 200 == 0:
            print "have processed %s items" % i
    return good[-1]

if __name__ == "__main__":
    filename = "knapsack_test.txt" # 147
    #filename = "knapsack1.txt"
    filename = "knapsack_big.txt"
    ks, ni, G = readfile(filename)
    res = big_kga(ks, ni, G)
    print res
