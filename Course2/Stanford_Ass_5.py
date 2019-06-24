print "Hello World!"

class node:
    def __init__(self, _id, edges = None):
        self.id = _id
        self.edges = edges or []
        self.explored = False
        self.finished = False
        self.finish = 0

class graph:
    def __init__(self):
        self.G = {}

    def original(self):
        f = open("SCC.txt")
        for line in f.readlines():
            (_id, out) = (int(n) for n in line.split(' ',1))
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
            node.finished = False

global res
res = []

def dfs(G, node):
    exp = 0
    stack = [node]
    while stack:
        node = stack[-1]
        if not node.explored:
            node.explored = True
            exp = exp + 1
            for edge in node.edges:
                if edge > 0 and not G[edge].explored:
                    stack.append(G[edge])
        else:
            if not node.finished:
                node.finished = True
                res.append(stack.pop())
            else:
                stack.pop()
    return exp

def dfs_loop(node_order):
    exo = []
    for node in node_order:
        if not node.explored:
            t = dfs(G, node)
            exo.append(t)
    return exo

if __name__ == "__main__":
    c = graph()
    c.original()
    c.reverse()
    G = c.G
    dfs_loop(sorted(G.values(),
                    key=lambda x:x.id,
                    reverse=True))
    finish_time = reversed(res)
    c.reverse()
    G = c.G
    result = dfs_loop(finish_time)
    result.extend([0]*5)
    print sorted(result, reverse=True)[:5]
