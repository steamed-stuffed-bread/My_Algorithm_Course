import random
import sys

def readfile(filename):
    f = open(filename)
    num_n, num_e = [int(x) for x in f.readline().split()]
    G = [[] for i in range(num_n)]
    for line in f.readlines():
        u, v, cost = [int(x) for x in line.split()]
        G[u-1].append((u-1, v-1, cost))
        G[v-1].append((v-1, u-1, cost))
    return G

def prim(G):
    n = len(G)
    MST = set()
    X = set()
    visit = [False for i in range(n)]

    s = random.randint(0, n-1)
    X.add(s)
    visit[s] = True

    while len(X) < n:
        cheapest = (-1,-1,sys.maxint)
        for u in X:
            for (u,v,cost) in G[u]:
                if not visit[v] and cost < cheapest[2]:
                    cheapest = (u,v,cost)
        X.add(cheapest[1])
        visit[cheapest[1]] = True
        MST.add(cheapest)
    return MST

if __name__ == "__main__":
    # filename = "edges_test.txt"  # 7
    filename = "edges.txt"
    G = readfile(filename)
    MST = prim(G)
    res = 0
    for e in MST:
        res = res + e[2]
    print res
