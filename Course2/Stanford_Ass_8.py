print "hello world!"

def read_data(filename):
    lines = open(filename).readlines()
    data = map(lambda x:int(x), lines)
    return data

def cal_2sum(data):
    ht = dict()
    for e in data:
        ht[e] = True

    res =  dict()
    processed = 0

    for x in ht.keys():
        processed = processed + 1
        for s in range(-10000, 10001):
            y = s - x
            if y != x and y in ht:
                res[s] = True
        if processed % 20000 == 0:
            print "Processed 20000x%s" % str(processed/20000)
            print "Current total is %s" % str(len(res))

    return len(res)

if __name__ == "__main__":
    data = read_data("2sum.txt")
    print "finished loading data"
    res = cal_2sum(data)
    print res
