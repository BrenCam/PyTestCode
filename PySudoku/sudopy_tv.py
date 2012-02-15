# -*- coding: utf-8 -*-
# Solve Every Sudoku Puzzle

# See http://norvig.com/sudoku.html

# Throughout this program we have:
#   r is a row,    e.g. 'A'
#   c is a column, e.g. '3'
#   s is a square, e.g. 'A3'
#   d is a digit,  e.g. '9'
#   u is a unit,   e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
#   g is a grid,   e.g. 81 non-blank chars, e.g. starting with '.18...7...
#   values is a dict of possible values, e.g. {'A1':'123489', 'A2':'8', ...}

# edited lines TV Tony Veijalainen 2010 plus these imports, all function removed as it is standard 
# ref: http://www.daniweb.com/code/snippet294304.html

#from __future__ import print_function
import os,sys
from time import clock

if (sys.version_info[0])==3:
    raw_input = input
## TV
    
def cross(A, B):
    return [a+b for a in A for b in B]

rows = 'ABCDEFGHI'
digits  =  cols = '123456789' # TV

squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)
peers = dict((s, set(s2 for u in units[s] for s2 in u if s2 != s))
             for s in squares)

def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False # Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values # Solved!
    # Chose the unfilled square s with the fewest possibilities
    _,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d))
                for d in values[s])

def assign(values, s, d):
    "Eliminate all the other values (except d) from values[s] and propagate."
    if all(eliminate(values, s, d2) for d2 in values[s] if d2 != d):
        return values
    else:
        return False

def eliminate(values, s, d):
    "Eliminate d from values[s]; propagate when values or places <= 2."
    if d not in values[s]:
        return values # Already eliminated
    values[s] = values[s].replace(d,'')
    if len(values[s]) == 0:
        return False # Contradiction: removed last value
    elif len(values[s]) == 1:
        # If there is only one value (d2) left in square, remove it from peers
        d2, = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    # Now check the places where d appears in the units of s
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values

def parse_grid(grid):
    "Given a string of 81 digits (or .0-), return a dict of {cell:values}"
    grid = [c for c in grid if c in '0.-N123456789']
    values = dict((s, digits) for s in squares) # Each square can be any digit
    for s,d in zip(squares, grid):
        if d in digits and not assign(values, s, d):
            return False
    printboard(values) #TV show result of first check
    return values

def solve_file(filename, sep='\n', action=lambda x: x):
    "Parse a file into a sequence of 81-char descriptions and solve them."
    t=clock() #TV
    results = [action(search(parse_grid(grid)))
               for grid in open(filename).read().strip().split(sep)]
    print("# Got %d out of %d" % (
          sum((r is not False) for r in results), len(results)))
    print ('Time taken %.3f s' % (clock()-t)) #TV
    return results

def solve(inpstr, sep='\n', action=lambda x: x):
    "Parse a input string into a sequence of 81-char descriptions and solve them."
    t=clock() #TV
    results = [action(search(parse_grid(grid)))
               for grid in inpstr.strip().split(sep)]
    print( "# Got %d out of %d" % (
          sum((r is not False) for r in results), len(results)))
    print ('Time taken %.3f s' % (clock()-t)) # TV
    return results


def printboard(values):
    "Used for debugging."
    width = 1+max(len(values[s]) for s in squares)
    line = '\n' + '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')# TV and or to if else
                      for c in cols) + (line if r in 'CF' else '')) # TV
    return values

def some(seq):
    for e in seq:
        if e: return e
    return False

# all definition removed, standard in Python


grid1  = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid2  = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
grid3  = '.....6....59.....82....8....45........3........6..3.54...325..6..................'
# World's hardest (Al Escargot)
grid4  = '1....7.9..3..2...8..96..5....53..9...1..8...26....4...3......1..4......7..7...3..'
grid5  = '500000009020100070008000300040600000000050000000207010003000800060004020900000005'
# test puzzle (difficult)    
grid6 = '600302000040000080000000000702600000000000054300000000080150000000080200000000700'



if __name__ == '__main__':
    ## TV
    if  len(sys.argv)>1:
        if os.path.isfile(sys.argv[1]):
            solve_file(sys.argv[1], action=printboard)
        elif len(sys.argv[1])>=81: # one sudoku in line
            solve(sys.argv[1], action=printboard)
    else: # interactive input line by line
        puzzle=grid3
        #for i in range(9):
            #row=''
            #while len(row) != 9:
                #row = raw_input('Row %i :' % (i+1))
                #if len(row) != 9:
                    #print("\n%i characters, mistake in line input again!" % len(row))
                #else:
                    #puzzle += row
        print('Solving..')
        solve(puzzle, action=printboard)
        
    raw_input('Push Enter')
    ## TV