print "Bellman Ford"

def readfile(filename):
    f = open(filename)
    m, n = [int(x) for x in f.readline().split()]
    edges = {}
    for line in f.readlines():
        u, v, weight = [int(x) for x in line.split()]
        edges[(u,v)] = weight
    return edges

if __name__ == '__main__':
    filename = 'g_test.txt' # -41
    G = readfile(filename)
    print G
