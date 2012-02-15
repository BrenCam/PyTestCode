#!/usr/bin/python
##Simplified version for 16 call grid - used for debugging/refactored to remove python idioms (if possible)
## To simplify:
##  - replace 'all' occurences with 'for in' loops  ('all', 'any' are Python 2.5 features)
##  - remove recursive calls - replace with iterations - easier to debug?
##  - replace list comprehensions (Ruby does not support these))
##
## BC: 9/2/2010
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

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]


rows = 'ABCD'
digits = '1234'

cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('AB','CD') for cs in ('12','34')])
#            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

for item in peers.iteritems():
    print item

################ Unit Tests ################

def test():
    "A set of unit tests for 2x2 grid."
    assert len(squares) == 16
    assert len(unitlist) == 12
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 7 for s in squares)
    assert units['A1'] == [['A1', 'B1', 'C1', 'D1'],
                           ['A1', 'A2', 'A3', 'A4'],
                           ['A1', 'A2', 'B1', 'B2']]
    assert peers['A1'] == set(['A3', 'A2', 'B1', 'B2', 'C1', 'D1', 'A4'])
    print '>>>>>> All tests pass. <<<<<<<'

################ Parse a Grid ################

def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    ## To start, every square can be any digit; then assign values from the grid.
    values = dict((s, digits) for s in squares)

    display(values)
    value_grid = grid_values(grid)
    #for s,d in grid_values(grid).items():
    for s,d in value_grid.items():
        print ">>parse_grid<<:   Square: %s; Digit: %s" %(s,d)

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
    assert len(chars) == 16
    return dict(zip(squares, chars))

################ Constraint Propagation ################

def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
 
    other_values = values[s].replace(d, '')
    print ">>assign<<:   Square: %s; Digit: %s; Other_Values: %s" %(s, d, other_values)
    
    # replace 'All' calls below
    #if all(eliminate(values, s, d2) for d2 in other_values):
    #    return values
    #else:
    #    return False
    
    err = False
    for d2 in other_values:
        if not eliminate(values, s, d2):
            return False        
    return values
    

def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""

    print ">>eliminate<<:   Square: %s; Digit: %s" %(s,d)
 
    if d not in values[s]:
        return values ## Already eliminated
    print ">>eliminate<<:   Removing digit: %s from candidates for cell: %s" %(d,s)
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
#    for u in units[s]:
#        dplaces = [s for s in u if d in values[s]]
#        if len(dplaces) == 0:
#            return False ## Contradiction: no place for this value
#        elif len(dplaces) == 1:
#            # d can only be in one place in unit; assign it there
#            if not assign(values, dplaces[0], d):
#                return False
#    return values

    ## replace preceding list comprehension with inline code
    dplaces = []
    for u in units[s]:
        if d in values[s]:
            for s in u:
               dplaces.append[s] 

    print ">> eliminate <<: dplaces: %s" %dplaces
    if len(dplaces) == 1:
              if not assign(values, dplaces[0], d):
                return False
    return values


################ Display as 2-D grid ################

def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*2)]*2)
    print line
    for r in rows:
        print ''.join(values[r+c].center(width)+('|' if c in '24' else '')
                      for c in cols)
        if r in 'BD': print line
    print

################ Search ################

def solve(grid): 
    return search(parse_grid(grid))

def search(values):
    "Using depth-first search and propagation, try all possible values."
    print ">>search<<:   performing depth-first search "
    if values is False:
        return False ## Failed earlier
    
    # rewrite below:
    #if all(len(values[s]) == 1 for s in squares):
    #    return values ## Solved!
    # replace 'all' refs with for loop 

    for s in squares:        
        if len(values[s]) == 1:
            return values ## Solved!
    
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    print ">> search <<:  cell: (%s) has the  fewest possibilities (%s): " %(n,s)
    return some(search(assign(values.copy(), s, d))
                for d in values[s])

################ Utilities ################

# ?? what does this do here ??
def some(seq):
    "Return some element of seq that is true."
    print ">>some<<:   iterating over search/assign loop (?via generator?) "
    for e in seq:
        if e: return e
    return False

def from_file(filename, sep='\n'):
    "Parse a file into a list of strings, separated by sep."
    return file(filename).read().strip().split(sep)

def shuffled(seq):
    "Return a randomly shuffled copy of the input sequence."
    seq = list(seq)
    random.shuffle(seq)
    return seq

################ System test ################

import time, random

#def solved(values):
#    "A puzzle is solved if each unit is a permutation of the digits 1 to 9."
#    def unitsolved(unit): 
#        print ">> solved <<:   puzzle solved "
#        return set(values[s] for s in unit) == set(digits)
#    return values is not False and all(unitsolved(unit) for unit in unitlist)

puzzle='1234341021434321'
puzzle='0004341021434300'
    
if __name__ == '__main__':
    test()
    print '>>> Begin <<<'
    
    print ">>> Puzzle: %s" %puzzle
    print ""
    display(solve(puzzle))
    #print solve(puzzle)

    
    print '>>> End <<<'

