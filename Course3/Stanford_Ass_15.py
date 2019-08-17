print "Hello World!"

def readfile(filename):
    freq = []
    f = open(filename)
    n = int(f.readline())
    for line in f.readlines():
        freq.append(int(line))
    return freq

def mwis(path):
    A = [0, path[0]]
    for i in range(2, len(path) + 1):
        A.append(max(A[i-1], A[i-2] + path[i-1]))
    return reconstruct(A,path)

def reconstruct(A,path):
    S = []
    target = [1,2,3,4,17,117,517,997]
    i = len(A) - 1
    while i > 1:
        if A[i-1] > A[i-2] + path[i-1]:
            i = i-1
            print "i-1 %s" % S
        else:
            S.append(i)
            i = i-2
            print "i-2 %s" % S
    if i == 1:
        S.append(1)
    ans = ''.join([str(int(bit in S)) for bit in target])
    return ans

if __name__ == "__main__":
    filename = "mwis_test.txt" # 10010000
    #filename = "mwis.txt"
    freq = readfile(filename)
    ans = mwis(freq)
    print ans
