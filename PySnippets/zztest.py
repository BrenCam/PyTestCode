# -*- coding: utf-8 -*-
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
#unitlist = ([cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
#unitlist = ([cross(rs, cs) for rs in ('ABC','DEF') for cs in ('123','456')])

unitlist = ([cross(rs, cs) for rs in ('AB','CD') for cs in ('12','34')])
#unitlist = ([cross(rs, cs) for rs in ('ABC') for cs in ('123')])

#units = dict((s, [u for u in unitlist if s in u])
#             for s in squares)
#peers = dict((s, set(sum(units[s],[]))-set([s]))
#             for s in squares)
ul = []
for rs in ('AB','CD'):
	for cs in ('12','34'):
		ul.append(cross(rs,cs))
		
print ul

def get_subgrids(rset, cset):
    # get subgrids for specified row and col sets
    # does the same as the following list comprehension
    #unitlist = ([cross(rs, cs) for rs in ('ABC','DEF') for cs in ('123','456')])
    
    #w/out list comprehension aproach
    ar = []
    res = []
    for r in rset:
	for c in cset:
	    for rr in r:
		for cc in c:
		    ar.append(rr+cc)
	    res.append(ar)
	    ar  =  []
    return res
    
    
################ Unit Tests ################

rs =  ['ABC','DEF', 'GHI']
cs = ['123','456','789']

sg  =  get_subgrids(rs,cs)
print sg
print unitlist
