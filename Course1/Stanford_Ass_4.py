# I refered to https://stackoverflow.com/questions/23825200/karger-min-cut-algorithm-in-python-2-7
import random
import copy
print "Hello World!"

def load(filename):
    data = open(filename, "r")
    G = {}
    for line in data:
        lst = [int(s) for s in line.split()]
        G[lst[0]] = lst[1:]
    return G

def choose_random(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(G[v1])
    return v1, v2

def Karger(G):
    length = []
    while len(G)>2:
        v1, v2 = choose_random(G)
        G[v1].extend(G[v2])
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1)
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
    for key in G.keys():
        length.append(len(G[key]))
    return length[0]

if __name__ == "__main__":
    G = load("KargerMincut.txt")
    #G = load("test.txt")
    i = 0
    best = 9999
    while i<100:
        data = copy.deepcopy(G)
        min_cut = Karger(data)
        if min_cut < best:
            best = min_cut
        i = i+1

    print best
