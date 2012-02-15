#!/usr/bin/python
# -*- coding: utf-8 -*-
##Simplified version for 16 call grid - used for debugging/refactored to remove python idioms (if possible)
## To simplify:
##  - replace 'all' occurences with 'for in' loops  ('all', 'any' are Python 2.5 features)
##  - remove recursive calls - replace with iterations - easier to debug?
##  - replace list comprehensions (Ruby does not support these))
##  - implement ruby generator ??
##
## BC: 9/5/2010
## Solve Every Sudoku Puzzle 

## See http://norvig.com/sudoku.html

## Throughout this program we have:
##   r is a row,    e.g. 'A'
##   c is a column, e.g. '3'
##   s is a square, e.g. 'A3'
##   d is a digit,  e.g. '9'
##   u is a unit,   e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
##   grid is a grid,e.g. 81 non-blank chars, e.g. starting with '.18...7...
##   values is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}

import os,sys
from time import clock


def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]


rows = 'ABCDEFGHI'
digits = '123456789'

cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

#for item in peers.iteritems():
    #print item
global assign_cnt
assign_cnt =  0
################ Unit Tests ################

def test():
    "A set of unit tests for 3x3 grid."
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print 'All tests pass.'

################ Parse a Grid ################

def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    ## To start, every square can be any digit; then assign values from the grid.
    values = dict((s, digits) for s in squares)

    #display(values)
    value_grid = grid_values(grid)
    #for s,d in grid_values(grid).items():
    for s,d in value_grid.items():
        #print ">>parse_grid<<:   Square: %s; Digit: %s" %(s,d)

        if d in digits:
            if not assign(values, s, d):
                return False      ## (Fail if we can't assign d to square s.)
    return values
       
#        if d in digits and not assign(values, s, d):
#            #display(values)
#            return False ## (Fail if we can't assign d to square s.)
#    return values

def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    print ">>grid_values<<:  recompute  dict  of poss values " 
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

################ Constraint Propagation ################

def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
 
    other_values = values[s].replace(d, '')
    #print ">>assign<<:   Square: %s; Digit: %s; Other_Values: %s" %(s, d, other_values)
    
    # replace 'All' calls below
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False
    
    #err = False
    #for d2 in other_values:
        #if not eliminate(values, s, d2):
            #return False        
    #return values
    
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

def zz_eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""

    #print ">>eliminate<<:   Square: %s; Digit: %s" %(s,d)
 
    if d not in values[s]:
        return values ## Already eliminated
    #print ">>eliminate<<:   Removing digit: %s from candidates for cell: %s" %(d,s)
    values[s] = values[s].replace(d,'')
    
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]

        #        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
        #            return False
        # replace preceding 'all' refs with code below
        for s2 in peers[s]:
            if not (eliminate(values, s2, d2)):
                return False

    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    global assign_cnt 
    #assign_cnt= 0
#    for u in units[s]:
#        dplaces = [s for s in u if d in values[s]]
#        if len(dplaces) == 0:
#            return False ## Contradiction: no place for this value
#        elif len(dplaces) == 1:
#            # d can only be in one place in unit; assign it there
#           assign_cnt += 1
#            print "Iteration Count: %s" %assign_cnt
#            if not assign(values, dplaces[0], d):
#                return False
#    return values  

   ## replace preceding list comprehension with inline code
   # code below here runs much slower than preceding code on grid6 test (14 secs vs 0.05 secs)
    dplaces = []
    for u in units[s]:
       if d in values[s]:
         
    
#    if d in values[s]:
#      for u in units[s]:
         
           for s in u:
               dplaces.append[s] 
               assign_cnt += 1
               #print "Iteration Count: %s" %assign_cnt   
               print "Iteration Count: "   
               
                             
           #if len(dplaces) == 0:
           #    return False
           if len(dplaces) == 1:
#               assign_cnt += 1
#               print "Iteration Count: %s" %assign_cnt             
               if not assign(values, dplaces[0], d):
                   return False
    return values  
               
    # if len(dplaces) == 0:
    #     return False
    #print ">> eliminate <<: dplaces: %s" %dplaces           
#    return values


################ Display as 2-D grid ################

def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    print line
    for r in rows:
        print ''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols)
        if r in 'CF': print line
    print

################ Search ################

def solve(grid): 
    return search(parse_grid(grid))

def search(values):
    "Using depth-first search and propagation, try all possible values."
    
    
    #print ">>search<<:   performing depth-first search "
    if values is False:
        return False ## Failed earlier
    
    # rewrite below:
    #if all(len(values[s]) == 1 for s in squares):
    #    return values ## Solved!
    # replace 'all' refs with for loop 

    done = True
    for s in squares:
        # bail out if any unsolved square - additional searching is required
        if  len(values[s]) != 1:
            done = False
            break
        #else:
        # only get here if all elements are squares have length = 1
        #    done = True
    if done:
        return values ## Solved!
    

    # rewrite below:
    # Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    #print ">> search <<:  cell: (%s) has the  fewest possibilities (%s): " %(n,s)
    return some(search(assign(values.copy(), s, d))
                for d in values[s])

#    for s in squares:
#        if len(values[s]) > 1:
            #n,s = min(len(values[s], s))
            # get the shortest entry in the possible value list
            # how to query a dictionary for this
            #n = min(len(values[s])
#            minval = min([ (values[x], x) for x in values])
            #minval = min([ len((values[x]), x) for x in values])
            #n,s = minval[0], minval[1]
#            s,n = get_candidate(values)
            
            #print ">> search <<:  cell: (%s) has the  fewest possibilities (%s): %s " %(n,s, values[s])

            # ??Rewrite this in section w/out generator ??
            #print ">> search <<:  values[s]: (%s) ; " %values[s]
            
            # Note: recode w/out generator ?? -  How ??
            # Create simple py  test w counter/Fib Series 

#            return some(search(assign(values.copy(), s, d))
#                       for d in values[s])
            

            # gets errors on some puzzles
            # code below is a substitute for the sequence/generator and 
            # appears to work
            
            #for d in values[s]:
                #r = search(assign(values.copy(), s, d))
                #if r:
                    #return r
            #return False
            
################ Utilities ################

def some(seq):
    for e in seq:
        if e: return e
    return False


# ?? what does this do here ??
#def some(seq):
    #"Return some element of seq that is true."
       
    ##print ">>some<<:   iterating over search/assign loop (?via generator?) "
    ## for expression in sequence
    #for e in seq:
        ##print ">>>> some:  call some"
        #if e:
            ##print ">>>> some:  return e"        
            #return e
    ##print ">>>> some:  return false"                
    #return False

def from_file(filename, sep='\n'):
    "Parse a file into a list of strings, separated by sep."
    return file(filename).read().strip().split(sep)

def shuffled(seq):
    "Return a randomly shuffled copy of the input sequence."
    seq = list(seq)
    random.shuffle(seq)
    return seq
        
def cmplen(x,y):
    # sort array by element [1]
    return cmp(x[1],y[1])

def get_candidate(d):
    
    # Build list/array of dict values 
    #dl = map(lambda x: len(x), d.itervalues())
    dl = map(lambda x: len(x), d.values())
    
    # get matching keys
    #dk = d.iterkeys()
    # create 
    #dk  = [k for k in d.iterkeys()]
    dk = d.keys()
    # build combined array of keys and string lengths
    lz = zip(dk, dl)
    #lzz = zip(dkk, dl)
    
    # remove elements w len = 1
    lf =  filter(lambda x: x[1] > 1, lz)
    
    # Need to sort by length (element [1] in array
    lf.sort(cmplen)
    #print '>> Done: filtered and sorted result array: %s' %lf
    
    #print "Next candidate is: %s; possible values: %s" %(lf[0], lf[1])  
    return lf[0][0], lf[0][1]    

################ System test ################

import time, random

#def solved(values):
#    "A puzzle is solved if each unit is a permutation of the digits 1 to 9."
#    def unitsolved(unit): 
#        print ">> solved <<:   puzzle solved "
#        return set(values[s] for s in unit) == set(digits)
#    return values is not False and all(unitsolved(unit) for unit in unitlist)

#grid1  = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
#puzzle  = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
#puzzle  = '.....6....59.....82....8....45........3........6..3.54...325..6..................'

grid1  = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid2  = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
grid3  = '.....6....59.....82....8....45........3........6..3.54...325..6..................'
# World's hardest (Al Escargot)
grid4  = '1....7.9..3..2...8..96..5....53..9...1..8...26....4...3......1..4......7..7...3..'
grid5  = '500000009020100070008000300040600000000050000000207010003000800060004020900000005'
# test puzzle (difficult)    
grid6 = '600302000040000080000000000702600000000000054300000000080150000000080200000000700'
 

# 9/7/2010 - Test results for preceding:
# Pass:  grid1(no phase 2 search required here), grid2, grid3, grid4, grid5, grid6 
# (grid6 takes a long time to run)
# Fail: 
if __name__ == '__main__':
    #test()
    
    # Import Psyco if available
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    # ...your code here...    
    
    
    print '>>> Begin <<<'
    puzzle =  grid3
    assign_cnt = 0
    print ">>> Puzzle: %s" %puzzle
    print ""
    # start timer
    t = clock()
    display(solve(puzzle))
    #print solve(puzzle)
    print ('Time taken %.3f s' % (clock()-t)) # TV

    
    print '>>> End <<<'

