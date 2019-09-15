import math
import random
print "2-set"

def readfile(filename):
    clauses = []
    f = open(filename)
    n = int(f.readline())
    for line in f.readlines():
        x, y = [int(e) for e in line.split()]
        clauses.append((x,y))
    return clauses

def papadimitrou(clauses):
    n = len(clauses)
    it_num = int(math.log(n,2))

    for i in range(it_num):
        print "%sth iteration" % i
        assignment = random_assignment(n)
        run = 2*n*n
        for i in range(run):
            unsat_index = unsatisfiable_index(clauses, assignment)
            if unsat_index == None:
                return "satisfiable"
            else:
                var_index = abs(clauses[unsat_index][random.randint(0,1)])-1
                assignment[var_index] = 1 - assignment[var_index]
    return "unsatifiable"

def unsatisfiable_index(clauses, assignment):
    for i in range(len(clauses)):
        if ((clauses[i][0] > 0 and assignment[abs(clauses[i][0])-1] == 0) or (clauses[i][0] < 0 and assignment[abs(clauses[i][0])-1] == 1)) \
                and \
           ((clauses[i][1] > 0 and assignment[abs(clauses[i][1])-1] == 0) or (clauses[i][1] < 0 and assignment[abs(clauses[i][1])-1] == 1)):
               return i
    return None

def random_assignment(n):
    return [random.randint(0,1) for e in range(n)]

if __name__ == '__main__':
    filename = '2set_test.txt'
    clauses = readfile(filename)
    res = papadimitrou(clauses)
    print "result is %s" % res
