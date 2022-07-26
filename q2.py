import csv
from pysat.solvers import Solver

#taking the user input for the dimension of sudoku

k = int(input("Enter the dimension of required sudoku: "))
s = Solver()


#now we create a model solution applying the constraints of 
# sudoku to an empty k dimension sudoku. this has been done similar to the 1st question algorithm


# assuring that each box has a number (atleat-atmost conditions as mentioned in the document)
for r in range(0, k*k):
    for c in range(0, k*k):
        list = []
        for m in range(1, k*k + 1):
            list.append(r*k*k*k*k + c*k*k + m)
        s.add_clause(list)

        for m in range(1, k*k + 1):
            for mm in range(1, k*k + 1):
                if(m != mm):
                    list = []
                    list.append((r*k*k*k*k + c*k*k + m)*(-1))
                    list.append((r*k*k*k*k + c*k*k + mm)*(-1))
                    s.add_clause(list)

# assuring that number m is present once in each row
for m in range(1, k*k + 1):
    for r in range(0, k*k):
        list = []
        for c in range(0, k*k):
            list.append(r*k*k*k*k + c*k*k + m)
        s.add_clause(list)

        for c in range(0, k*k):
            for cc in range(0, k*k):
                if(cc != c):
                    list = []
                    list.append((r*k*k*k*k + c*k*k + m)*(-1))
                    list.append((r*k*k*k*k + cc*k*k + m)*(-1))
                    s.add_clause(list)


# assuring that number m is present once in each column
for m in range(1, k*k + 1):
    for c in range(0, k*k):
        list = []
        for r in range(0, k*k):
            list.append(r*k*k*k*k + c*k*k + m)
        s.add_clause(list)

        for r in range(0, k*k):
            for rr in range(0, k*k):
                if(rr != r):
                    list = []
                    list.append((r*k*k*k*k + c*k*k + m)*(-1))
                    list.append((rr*k*k*k*k + c*k*k + m)*(-1))
                    s.add_clause(list)


# assuring that number m is present once in each box
qx = 0
qy = 0

while(qx < k*k - k + 1):
    while(qy < k*k - k + 1):
        for m in range(1, k*k+1):
            list = []
            for x in range(0, k):
                for y in range(0, k):
                    list.append((qx+x)*k*k*k*k + (qy+y)*k*k + m)
            s.add_clause(list)

        for m in range(1, k*k + 1):
            for x in range(0, k):
                for y in range(0, k):
                    for xx in range(0, k):
                        for yy in range(0, k):
                            if((xx != x) or (yy != y)):
                                list = []
                                list.append(((qx + x)*k*k*k*k + (qy + y)*k*k + m)*(-1))
                                list.append(((qx + xx)*k*k*k*k + (qy + yy)*k*k + m)*(-1))
                                s.add_clause(list)
        qy = qy + k
    qx = qx + k


sol = []
changecount = 0
s.solve()
sol = s.get_model()
flagcount = 1
changecount = 0
eflag = 0

# Now, we iterate through the unit cells of the filledsudoku until no more deletions are possible.
#these deletions are done if they dont affect the uniqueness of the solution

while (1 > 0):
    changecount = 0
    for bb in range(0, k*k):
        for aa in range(0, k*k):
            count = 1
            while(count <= k*k):
                eflag = 0
                if (sol[bb*k*k*k*k + aa*k*k + count - 1] > 0):
                    flagcount = count
                    eflag = 1
                count = count + 1
            g = Solver()
            g = s
            if (eflag == 0):
                continue
            for fb in range(0, k*k):
                for fa in range(0, k*k):
                    if((fb != bb) or (fa != aa)):
                        for fc in range(1, k*k + 1):
                            g.add_clause([fb*k*k*k*k + fa*k*k + fc])
                    else:
                        g.add_clause([(fb*k*k*k*k + fa*k*k + flagcount)*(-1)])
            if(not g.solve()):
                sol[bb*k*k*k*k + aa*k*k + flagcount - 1] = -sol[bb*k*k*k*k + aa*k*k + flagcount - 1]
                changecount = changecount + 1
            g.delete()
    if changecount == 0:
        break

##now that we have a unique sudoku problem, we can generate its pair by simply 
# shifting the face values of the numbers by 1. i.e, changing 1 to 2 , 2 to 3, ..., 9 to 1.


##these pair of sudoku have been printed to different csv files as follows:
rowlist = []

filename = "solutionsudoku5a.csv"
csvfile = open(filename, 'w')
csvwriter = csv.writer(csvfile)

for sb in range(0, k*k):
    for sa in range(0, k*k):
        count = 1
        eflag = 0
        while(count <= k*k and eflag != 1):
            if (sol[sb*k*k*k*k + sa*k*k + count - 1] > 0):
                flagcount = count
                eflag = 1
            count = count + 1
        if(eflag == 0):
            rowlist.append(0)
        else:
            rowlist.append(flagcount)
    csvwriter.writerow(rowlist)
    rowlist = []


filename = "solutionsudoku5b.csv"
csvfile = open(filename, 'w')
csvwriter = csv.writer(csvfile)
eflag = 0

for sb in range(0, k*k):
    for sa in range(0, k*k):
        count = 1
        eflag = 0
        while(count <= k*k and eflag != 1):
            if (sol[sb*k*k*k*k + sa*k*k + count - 1] > 0):
                flagcount = count
                eflag = 1
            count = count + 1
        if(eflag == 0):
            rowlist.append(0)
        else:
            if(flagcount == k*k):
                flagcount = 1
            else:
                flagcount = flagcount + 1
            rowlist.append(flagcount)
    csvwriter.writerow(rowlist)
    rowlist = []
