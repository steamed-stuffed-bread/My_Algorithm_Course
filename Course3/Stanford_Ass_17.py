import sys
print "Bellman Ford"
# https://github.com/jamesguoxin/Algorithms

def readfile(filename):
    f = open(filename)
    nv, ne = [int(x) for x in f.readline().split()]
    edges = {}
    for line in f.readlines():
        u, v, weight = [int(x) for x in line.split()]
        edges[(u,v)] = weight
    return edges, nv

def Floyed_Warshall(G, nv):
    bound = nv+1
    A = [[sys.maxint for i in range(bound)] for j in range(bound)]
    last_A = A
    for i in range(bound):
        for j in range(bound):
            if i == j:
                last_A[i][j] = 0
            elif (i,j) in G.keys():
                last_A[i][j] = G[(i,j)]
    for k in range(1,bound):
        for i in range(1,bound):
            for j in range(1,bound):
                A[i][j] = min(last_A[i][j], last_A[i][k]+last_A[k][j])
                if i == j:
                    if A[i][j] < 0:
                        return "Graph has a nagetive cycle!"
    return min(min(A, key=lambda x:min(x)))

#def Bellman_Ford(G, nv):

if __name__ == '__main__':
    filename = 'g_test.txt' # -41
    G, nv = readfile(filename)
    res = Floyed_Warshall(G, nv)
    print res
