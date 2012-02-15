# -*- coding: utf-8 -*-
def cross(A, B):
    return [a+b for a in A for b in B]


def test():
    "A set of unit tests."
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
    
# 
#digits = '1234'
#rows = 'ABCD'
#r = cross (A,B)

digits   = '123456789'
rows     = 'ABCDEFGHI'


if __name__ == '__main__':

    cols     = digits
    
    squares  = cross(rows, cols)
    ulist_a = [cross(rows, c) for c in cols]
    ulist_b = [cross(r, cols) for r in rows]
    ulist_c = [cross(rs, cs) for rs in ('AB','CD') for cs in ('12','34')]
    #ulist_c = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
    
    
    unitlist = ([cross(rows, c) for c in cols] +
		[cross(r, cols) for r in rows] +
		[cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
		#[cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
    units = dict((s, [u for u in unitlist if s in u]) 
		 for s in squares)
    peers = dict((s, set(sum(units[s],[]))-set([s]))
		 for s in squares)
    
    
    print '>>> Start <<<\n'
    
    test()
    
    print 'digits: \n',  digits
    print 'rows: \n',  rows
    
    print 'squares: \n',  squares
    
    print 'unitlist: A: \n',  ulist_a
    
    print 'unitlist: B: \n',  ulist_b
    
    print 'unitlist: C: \n',  ulist_c
    
    #print 'units: %s\n',  units
    
    #print 'peers: %s\n',  peers
    
    #   print '>>> Total # of iterations/recursion calls processed =  %s <<<\n' %itercnt
    
    print '>>> Done <<<\n'
