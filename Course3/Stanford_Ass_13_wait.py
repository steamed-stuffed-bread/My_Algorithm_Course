import copy
def b2d(x):
    l = len(x)
    res = 0
    for i in range(l):
        res = res + x[l-i-1]*(2**i)
    return res

class UF:
    def __init__(self, lines, N, b):
        self.b = b
        self.N = N
        self.lines = lines
        self.codes = {b2d(key):key for key in self.lines}
        self.clusters = {key:key for key in set(self.codes.keys())}
        self.neighbors = {key:self.neighber(key) for key in set(self.codes.keys())}
    def find(self,q):
        return self.clusters[q]
    def n(self):
        num = 0
        for key in self.clusters.keys():
            if key == self.clusters[key]:
                num = num + 1
        return num
    def distance(self,i,j):
        d = 0
        
        l1 = self.codes[i]
        l2 = self.codes[j]

        for i in range(self.b):
            if l1[i] != l2[i]:
                d = d+1
        return d
    def neighber(self,q):
        neighber1 = []
        neighber2 = []

        code = self.codes[q]

        for i in range(self.b):
            swap_1 = copy.copy(code)
            if code[i] == 1:
                swap_1[i] = 0
            else:
                swap_1[i] = 1
            neighber1.append(b2d(swap_1))
        for i in range(self.b):
            for j in range(i+1,self.b):
                if j!=i:
                    swap_2 = copy.copy(code)
                    if code[i] == 1:
                        swap_2[i] = 0
                    else:
                        swap_2[i] = 1
                    if code[j] == 1:
                        swap_2[j] = 0
                    else:
                        swap_2[j] = 1
                    neighber2.append(b2d(swap_2))
        neighber = neighber1+neighber2
        return neighber
    def union(self,p,q):
        pid = self.find(p)
        qid = self.find(q)

        neighber_p = self.neighber(p)
        for e in neighber_p:
            try:
                z = self.clusters[e]
            except KeyError:
                continue
            if self.find(z) == qid:
                self.clusters[z] = pid

def readfile(filename):
    f = open(filename)
    n,bi = [int(x) for x in f.readline().split()]
    lines = []
    for line in f.readlines():
        lines.append([int(b) for b in line.split()])
    return n,bi,lines

def clustering(lines, n, b):
    uf = UF(lines,n,b)
    decimal = list(map(b2d, lines))

    cnt = 0

    for p in set(decimal):
        cnt = cnt + 1
        pn = uf.neighbors[p]
        for q in pn:
            try:
                d_pq = uf.distance(p,q)
            except KeyError:
                continue
            #if d_pq >= 1 and d_pq <=2:
            if d_pq <=2:
                uf.union(p,q)
        if cnt % 200 == 0:
            print "Processing... %s completed" % cnt
    return uf.n()

if __name__ == "__main__":
    #filename = "clustering_big_test.txt" # 15
    #filename = "clustering_big_test1.txt" # 15
    filename = "clustering_big_test2.txt" # 3
    #filename = "clustering_big.txt"
    n,b,lines = readfile(filename)
    res = clustering(lines, n, b)
    print res
