print "Hello World!"

class node:
    def __init__(self, _id, edges = None):
        self.id = _id
        self.edges = edges or []
        self.explored = False
        self.finish = 0

class graph:
    def __init__(self):
        self.G = {}

    def original(self):
        f = open("test.txt")
        for line in f.readlines():
            (_id, out) = (int(n) for n in line.split(" "))
            if _id not in self.G:
                self.G[_id] = node(_id, edges = [out])
            else:
                self.G[_id].edges.append(out)

            if out not in self.G:
                self.G[out] = node(out, edges = [-_id])
            else:
                self.G[out].edges.append(-_id)

    def reverse(self):
        for node in self.G.values():
            node.edges = [-edge for edge in node.edges]
            node.explored = False

def dfs(G, node):
    exp = 0
    stack = [node]
    while stack:
        node = stack.pop()
        if not node.explored:
            node.explored = True
            exp = exp + 1
            for edge in node.edges:
                if edge > 0 and not G[edge].explored:
                    stack.append(G[edge])
    return exp

def dfs_loop(node_order):
    res = []
    for node in node_order:
        if not node.explored:
            print "Exploring the graph from node %s" % node.id
            t = dfs(G, node)
            node.finish = t
            res.append(t)
    return res

if __name__ == "__main__":
    c = graph()
    c.original()
    c.reverse()
    G = c.G
    res = dfs_loop(sorted(G.values(),
                    key=lambda x:x.id,
                    reverse=True))
    print res
    #c.reverse()
    #G = c.G
    #result = dfs_loop(sorted(G.values(),
    #                  key=lambda x:x.finish,
    #                  reverse=True))
    #print result
