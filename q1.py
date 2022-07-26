import csv
import math
from pysat.solvers import Solver

s = Solver()
list = []
ncol = 0
nrow = 0

# for the first sudoku:
# the 2 sudoku inputs are taken from 2 different csv files.
# already mentioned values in the sudoku problem have been directly added as clauses and 
# the atleast-atmost condition clauses has been applied other empty cells 

filename = "sudoku1.csv"

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    k = int(csvreader.line_num)
    k = int(math.sqrt(k))

    for row in csvreader:
        ncol = 0
        while (ncol < k*k):
            if (row[ncol] != 0):
                list.append(nrow*k*k*k*k + ncol*k*k + row[ncol])
                s.add_clause(list)
                list = []

            else:
                for i in range(1, k*k+1):
                    list.append(nrow*k*k*k*k + ncol*k*k + i)
                s.add_clause(list)
                list = []

                for a in range(1, k*k + 1):
                    for b in range(1, k*k + 1):
                        list.append((nrow*k*k*k*k + ncol*k*k + a)*(-1))
                        list.append((nrow*k*k*k*k + ncol*k*k + b)*(-1))
                        s.add_clause(list)
                        list = []

            ncol = ncol + 1
        nrow = nrow + 1

list = []

nrow = 0
ncol = 0

# assuring that number m is present once in each row
# simply clauses have been added as per the atleast-atmost 
# condition decribed in the document
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
# simply clauses have been added as per the atleast-atmost 
# condition decribed in the document
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
# simply clauses have been added as per the atleast-atmost 
# condition decribed in the document
qx = 0
qy = 0

while(qx < k*k - k + 1):
    while(qy < k*k - k + 1):
        for mp in range(1, k*k+1):
            list = []
            for x in range(0, k):
                for y in range(0, k):
                    list.append((qx+x)*k*k*k*k + (qy+y)*k*k + mp)
            s.add_clause(list)

        for mu in range(1, k*k+1):
            for x in range(0, k):
                for y in range(0, k):
                    for xx in range(0, k):
                        for yy in range(0, k):
                            if((xx != x) or (yy != y)):
                                list = []
                                list.append(((qx + x)*k*k*k*k + (qy + y)*k*k + mu)*(-1))
                                list.append(((qx + xx)*k*k*k*k + (qy + yy)*k*k + mu)*(-1))
                                s.add_clause(list)
        qy = k+qy

    qx = k+qx

# for the second sudoku:
# clauses added completely similar to the first sudoku

filename = "sudoku2.csv"

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    k = int(csvreader.line_num)
    k = int(math.sqrt(k))

    for row in csvreader:
        ncol = 0
        while (ncol < k*k):
            if (row[ncol] != 0):
                list.append(k*k*k*k*k*k + nrow*k*k*k*k + ncol*k*k + row[ncol])
                s.add_clause(list)
                list = []

            else:
                for i in range(1, k*k+1):
                    list.append(k*k*k*k*k*k + nrow*k*k*k*k + ncol*k*k + i)
                s.add_clause(list)
                list = []

                for a in range(1, k*k + 1):
                    for b in range(1, k*k + 1):
                        list.append(
                            (k*k*k*k*k*k + nrow*k*k*k*k + ncol*k*k + a)*(-1))
                        list.append(
                            (k*k*k*k*k*k + nrow*k*k*k*k + ncol*k*k + b)*(-1))
                        s.add_clause(list)
                        list = []

            ncol = ncol + 1
        nrow = nrow + 1

list = []

nrow = 0
ncol = 0

# assuring that number m is present once in each row
for m in range(1, k*k + 1):
    for r in range(0, k*k):
        list = []
        for c in range(0, k*k):
            list.append(k*k*k*k*k*k + r*k*k*k*k + c*k*k + m)
        s.add_clause(list)

        for c in range(0, k*k):
            for cc in range(0, k*k):
                if(cc != c):
                    list = []
                    list.append((k*k*k*k*k*k + r*k*k*k*k + c*k*k + m)*(-1))
                    list.append((k*k*k*k*k*k + r*k*k*k*k + cc*k*k + m)*(-1))
                    s.add_clause(list)


# assuring that number m is present once in each column
for m in range(1, k*k + 1):
    for c in range(0, k*k):
        list = []
        for r in range(0, k*k):
            list.append(k*k*k*k*k*k + r*k*k*k*k + c*k*k + m)
        s.add_clause(list)

        for r in range(0, k*k):
            for rr in range(0, k*k):
                if(rr != r):
                    list = []
                    list.append((k*k*k*k*k*k + r*k*k*k*k + c*k*k + m)*(-1))
                    list.append((k*k*k*k*k*k + rr*k*k*k*k + c*k*k + m)*(-1))
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
                    list.append(k*k*k*k*k*k + (qx+x)*k*k*k*k + (qy+y)*k*k + m)
            s.add_clause(list)

        for m in range(1, k*k + 1):
            for x in range(0, k):
                for y in range(0, k):
                    for xx in range(0, k):
                        for yy in range(0, k):
                            if((xx != x) and (yy != y)):
                                list = []
                                list.append((k*k*k*k*k*k + (qx + x)*k*k*k*k + (qy + y)*k*k + m)*(-1))
                                list.append((k*k*k*k*k*k + (qx + xx)*k*k*k*k + (qy + yy)*k*k + m)*(-1))
                                s.add_clause(list)
        qy = qy + k
    qx = qx + k


# adding the mutual non-equivalence condition between the two sudokus:
list = []

for m in range(1, k*k + 1):
    for c in range(0, k*k):
        for r in range(0, k*k):
            list.append((k*k*k*k*k*k + r*k*k*k*k + c*k*k + m)*(-1))
            list.append((r*k*k*k*k + c*k*k + m)*(-1))
            s.add_clause(list)
            list = []


# printing the required output:

if (s.solve()):
    count = 0
    number = 1
    solution = []
    solution = s.get_model()
    for h in range(1, 3):
        for f in range(1, k*k + 1):
            for u in range(1, k*k + 1):
                number = 1
                for e in range(1, k*k + 1):
                    if(list[count] > 0):
                        print(number, end=" ")
                    count = count + 1
                    number = number + 1
            print("")
        print("")
else:
    print("None")
