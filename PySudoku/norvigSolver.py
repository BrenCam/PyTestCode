class   norvigSolver:
            
## Solve Every Sudoku Puzzle

## See http://norvig.com/sudoku.html

## Throughout this program we have:
##   r is a row,    e.g. 'A'
##   c is a column, e.g. '3'
##   s is a square, e.g. 'A3'
##   d is a digit,  e.g. '9'
##   u is a unit,   e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
##   g is a grid,   e.g. 81 non-blank chars, e.g. starting with '.18...7...
##   values is a dict of possible values, e.g. {'A1':'123489', 'A2':'8', ...}


    #rows = 'ABCDEFGHI'
    #cols = '123456789'
    digits   = '123456789'
    squares =""
    units =""
    peers =""
    

    def solve(self, puzzle):

	# convert result to formatted string
        rsltdict = self.search(self.parse_grid(puzzle))
	return self.formatResults (rsltdict)
        
    def formatResults (self,thedict):
	keys = thedict.keys()
	keys.sort()
	l1 = map (thedict.get, keys)
	result = ''.join (l1)
	return result        
          
    def cross(self,A, B):
        return [a+b for a in A for b in B]    
    
    def __init__ (self):            

        rows = 'ABCDEFGHI'
        cols = '123456789'
        #digits   = '123456789' 
                
        self.squares  = self.cross(rows, cols)
        unitlist = ([self.cross(rows, c) for c in cols] +
                    [self.cross(r, cols) for r in rows] +
                    [self.cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
        self.units = dict((s, [u for u in unitlist if s in u]) 
                     for s in self.squares)
        self.peers = dict((s, set(s2 for u in self.units[s] for s2 in u if s2 != s))
                     for s in self.squares)

    def search(self,values):
        "Using depth-first search and propagation, try all possible values."
        if values is False:
            return False ## Failed earlier
        if self.all(len(values[s]) == 1 for s in self.squares): 
            return values ## Solved!
        ## Chose the unfilled square s with the fewest possibilities
        _,s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return self.some(self.search(self.assign(values.copy(), s, d)) 
                    for d in values[s])
    
    def assign(self, values, s, d):
        "Eliminate all the other values (except d) from values[s] and propagate."
        if self.all(self.eliminate(values, s, d2) for d2 in values[s] if d2 != d):
            return values
        else:
            return False
    
    def eliminate(self, values, s, d):
        "Eliminate d from values[s]; propagate when values or places <= 2."
        if d not in values[s]:
            return values ## Already eliminated
        values[s] = values[s].replace(d,'')
        if len(values[s]) == 0:
            return False ## Contradiction: removed last value
        elif len(values[s]) == 1:
            ## If there is only one value (d2) left in square, remove it from peers
            d2, = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False
        ## Now check the places where d appears in the units of s
        for u in self.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                # d can only be in one place in unit; assign it there
                if not self.assign(values, dplaces[0], d):
                    return False
        return values
                        
    def parse_grid(self, grid):
        "Given a string of 81 digits (or .0-), return a dict of {cell:values}"
        grid = [c for c in grid if c in '0.-123456789']
        values = dict((s, self.digits) for s in self.squares) ## Each square can be any digit
        for s,d in zip(self.squares, grid):
            if d in self.digits and not self.assign(values, s, d):
                return False
        return values
    
    #def solve_file(self, filename, sep='\n', action=lambda x: x):
        #"Parse a file into a sequence of 81-char descriptions and solve them."
        #results = [action(search(parse_grid(grid)))
                   #for grid in file(filename).read().strip().split(sep)]
        #print "## Got %d out of %d" % (
              #sum((r is not False) for r in results), len(results))
        #return results
                
    def all(self,seq):
        for e in seq:
            if not e: return False
        return True
    
    def some(self,seq):
        for e in seq:
            if e: return e
        return False
    
# test puzzle (difficult)    
puzzle='600302000040000080000000000702600000000000054300000000080150000000080200000000700'
# World's hardest (Al Escargot)
#puzzle='1....7.9..3..2...8..96..5....53..9...1..8...26....4...3......1..4......7..7...3..'
#puzzle ='.....6....59.....82....8....45........3........6..3.54...325..6..................'

#puzzle='500000009020100070008000300040600000000050000000207010003000800060004020900000005'
if __name__ == '__main__':
    
    # solve_file("sudoku_hard.txt", action=printboard)
    #  solve_file("SudokuTestData.txt", action=printboard)
    solver = norvigSolver()
    
    result = solver.solve(puzzle)
    #result = search(puzzle)
    print ('Puzzle:     ' + puzzle)
    print ('Solution:   ' + str(result))
    
    #solver.printresults (result)
   
## References used:
## http://www.scanraid.com/BasicStrategies.htm
## http://www.krazydad.com/blog/2005/09/29/an-index-of-sudoku-strategies/
## http://www2.warwick.ac.uk/fac/sci/moac/currentstudents/peter_cock/python/sudoku/
