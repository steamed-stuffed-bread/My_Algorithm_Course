class UF:
    def __init__(self, N):
        self.clusters = {key:key for key in range(1, N+1)}
    def find(self, q):
        return self.clusters[q]
    def union(self,p,q):
        pid = self.find(p)
        qid = self.find(q)
        for e in self.clusters:
            if qid == self.find(e):
                self.clusters[e] = pid
    def n(self):
        return len(set(self.clusters.values()))

def readfile(filename):
    f = open(filename)
    n = int(f.readline())
    edges = []
    for line in f.readlines():
        u,v,cost = [int(x) for x in line.split()]
        edges.append((u, v, cost))
    return edges,n

def clustering(edges, n, t):
    criterian = lambda (u,v,cost):cost
    edges.sort(key = criterian)

    uf = UF(n)
    T = set()
    for e in edges:
        u,v = e[0:2]
        if uf.find(u) != uf.find(v):
            uf.union(u,v)
            T = T.union({e})
        if uf.n() == t:
            break

    c_edges = [e for e in edges if uf.find(e[0])!=uf.find(e[1])]
    spacing = min([e[2] for e in c_edges])

    clusters = {}
    for e in uf.clusters:
        if uf.find(e) not in clusters.keys():
            clusters[uf.find(e)] = [e]
        else:
            clusters[uf.find(e)].append(e)

    return clusters, spacing

if __name__ == "__main__":
    #filename = "clustering_test.txt"
    filename = "clustering1.txt"
    edges,n = readfile(filename)
    target = 4
    tree, res = clustering(edges,n,target)
    print "The result cluster crossing edges are %s" % tree
    print "The result spacing is %s" % res
