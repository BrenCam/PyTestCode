# -*- coding: utf-8 -*-
def	cross(A, B):

	return [a+b for a in A for b in B]


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
    
if __name__ == '__main__':

  digits = '1234'
  rows = 'ABCD'
  cols = digits

  squares  = cross(rows, cols)
  ulist_a = [cross(rows, c) for c in cols]
  ulist_b = [cross(r, cols) for r in rows]
  ulist_c = [cross(rs, cs) for rs in ('AB','CD') for cs in ('12','34')]
  
  ulc = []
  for rs in ('AB','CD'):
    for cs in ('12','34'):
      ulc.append(cross(rs,cs))

  unitlist = ([cross(rows, c) for c in cols] +
              [cross(r, cols) for r in rows] +
              ulc)
#              [cross(rs, cs) for rs in ('AB','CD') for cs in ('12','34')])
#            [cross(rs, cs) for rs in ('AB','CD') for cs in ('12','34')])
  units = dict((s, [u for u in unitlist if s in u]) 
               for s in squares)
  peers = dict((s, set(sum(units[s],[]))-set([s]))
               for s in squares)

  print '>>> Start <<<\n'

  print 'Square 0 Peer List: ' , squares[0], peers[squares[0]]
  print 'Peer Length: \n' , len(peers[squares[0]]) 

  print 'Units - "A1"', units['A1']

  test()

  print 'digits: \n',  digits
  print 'rows: \n',  rows

  print 'squares: \n',  squares

  print 'unitlist: A: \n',  ulist_a

  print 'unitlist: B: \n',  ulist_b

  print 'unitlist: C: \n',  ulist_c
  
  print 'ulc: C: \n',  ulc
  
  #print 'units: %s\n',  units

  #print 'peers: %s\n',  peers

  #   print '>>> Total # of iterations/recursion calls processed =  %s <<<\n' %itercnt

  print '>>> Done <<<\n'
