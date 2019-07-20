def readfile(filename):
    f = open(filename)
    G = []
    n = int(f.readline())
    for line in f.readlines():
        w, l = [int(x) for x in line.split()]
        G.append((w,l))
    return G

def greedy_schedule(jobs, law, criterian, reverse = True):
    jobs.sort(key = law, reverse = reverse)
    jobs.sort(key = criterian, reverse = reverse)

    timeline = 0
    score = 0

    for (w,l) in jobs:
        timeline = timeline + l
        score = score + timeline*w

    return score

if __name__ == "__main__":
    #filename = "jobs_test.txt"  # 68615 67247
    filename = "jobs.txt"
    jobs = readfile(filename)

    criterian_1 = lambda (w,l):(w-l)
    criterian_2 = lambda (w,l):(float(w)/l)

    criterian_w = lambda (w,l):w

    print greedy_schedule(jobs, criterian_w, criterian_1)
    print greedy_schedule(jobs, criterian_w, criterian_2)
