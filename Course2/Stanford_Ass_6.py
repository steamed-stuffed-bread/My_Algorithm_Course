print "Hello World!"

def read(filename):
    f = open(filename)
    G = []
    for line in f.readlines():
        G.append([])
        tup = line.split()
        for ele in tup[1:]:
            v = int(tup[0])-1
            n, d = ele.split(",",1)
            G[v].append((int(n)-1, int(d))) 
    return G

def emin(q,w):
    i = 0
    j = 1
    m = w[q[0]]

    while j<len(q):
        if w[q[j]] < m:
            i = j
            m = w[q[j]]
        j = j+1
    res = q[i]
    q[i] = q[-1]
    q.pop()
    return res

def dijkstra(G):
    w = [1000000]*len(G)
    w[0] = 0
    vis = [False]*len(G)
    q = [i for i in range(len(G))]

    while len(q)>0:
        v = emin(q, w)
        vis[v] = True

        for ele in G[v]:
            n, lenth = ele
            if not vis[n]:
                w[n] = min(w[n], w[v] + lenth)

    return w

if __name__ == "__main__":
    G = read("dijkstraData.txt")
    #G = read("input_random_10_16.txt")
    desired = [7,37,59,82,99,115,133,165,188,197]
    sl = dijkstra(G)
    res = []
    for i in desired:
        res.append(sl[i-1])

    print res
