print "Hello World!"

def readfile(filename):
    freq = []
    f = open(filename)
    n = int(f.readline())
    for line in f.readlines():
        freq.append(int(line))
    return n, freq

class HuffmanNode:
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
    def isleft(self):
        #print "compare %s with %s" % (self.freq, self.father.left.freq)
        return self == self.father.left

def buildtree(nodes):
    q = nodes[:]
    while len(q) > 1:
        q.sort(key=lambda x:x.freq)
        right = q.pop(0)
        left = q.pop(0)
        father = HuffmanNode(right.freq+left.freq)
        father.left = left
        father.right = right
        left.father = father
        right.father = father
        q.append(father)
        #print "%s is father, %s is left, %s is right" % (father.freq, left.freq, right.freq)
    q[0].father = None
    return q[0]

def encoding(nodes, root):
    codes = ['' for i in range(len(nodes))]
    for i in range(len(nodes)):
        tmp = nodes[i]
        while tmp != root:
            if tmp.isleft():
                codes[i] = '0'+codes[i]
            else:
                codes[i] = '1'+codes[i]
            tmp = tmp.father
    return codes

if __name__ == "__main__":
    #filename = "huffman_test.txt" # 9 4
    filename = "huffman.txt"
    n, freq = readfile(filename)
    nodes = [HuffmanNode(f) for f in freq]
    root = buildtree(nodes)
    codes = encoding(nodes, root)
    len_codes = [len(code) for code in codes]
    print "the maximum length is %s" % max(len_codes)
    print "the minimum length is %s" % min(len_codes)
    #for e in zip(freq,codes):
    #    print "%s huffman code is %s" % (e[0],e[1])
