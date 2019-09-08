import math
print "tsp heuristic not right"
#https://github.com/shaiwalsachdev/Algorithms---Stanford-University/tree/master/Course%204-Shortest%20Paths%20Revisited%2C%20NP-Complete%20Problems%20and%20What%20To%20Do%20About%20Them/Week%203

def readfile(filename):
    f = open(filename)
    n = int(f.readline())
    vis = [0 for i in range(n)]
    cs = []
    for line in f.readlines():
        idx, x, y = [float(e) for e in line.split()]
        cs.append((x,y))
    return cs,vis

class Solution:
    def __init__(self,vis,cs):
        self.vis = vis
        self.cs = cs
        self.n = len(cs)
        self.INF = 99999999

    def euc(self, city1,city2):
        return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

    def findnext(self, cs,vis,current):
        min_dis = self.INF
        dis = 0
        n_idx = -1
        for j in range(self.n):
            if j!=current:
                dis = self.euc(cs[current],cs[j]);
                if dis< min_dis and vis[j]==0:
                    min_dis = dis
                    n_idx = j
        return n_idx,min_dis

    def TSP(self, cs, vis):
        cur = 0
        vis[cur] = 1
        n = len(cs)
        lenth = 0
        for i in range(1, n):
            vis[cur] = 1
            cur, m_dis = self.findnext(cs,vis,i)
            lenth = lenth + m_dis

        lenth = lenth + self.euc(cs[cur], cs[0])
        return lenth

if __name__ == '__main__':
    filename = "nn.txt" #22
    cs,vis = readfile(filename)
    c = Solution(vis,cs)
    res = c.TSP(cs, vis)
    print res

