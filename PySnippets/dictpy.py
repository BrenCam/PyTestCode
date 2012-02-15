#!/usr/bin/python
# dictpy.py

def cmplen(x,y):
    # sort array by element [1]
    return cmp(x[1],y[1])

def get_candidate(d):
    
    # Build list/array of dict values 
    dl = map(lambda x: len(x), d.itervalues())
    # get matching keys
    #dk = d.iterkeys()
    # create 
    dk  = [k for k in d.iterkeys()]
    # build combined array of keys and string lengths
    lz = zip(dk, dl)
    # remove elements w len = 1
    lf =  filter(lambda x: x[1] > 1, lz)
    
    # Need to sort by length (element [1] in array
    lf.sort(cmplen)
    print '>> Done: filtered and sorted result array: %s' %lf
    
    print "Next candidate is: %s; possible values: %s" %(lf[0], lf[1])  
    return lf[0][0], lf[0][1]    
    
if __name__ == '__main__':
    
    values = {'A1': '4', 'A2': '1679', 'G2': '89', 'B2': '345'}
  
    print '>>> Begin <<<'
    get_candidate(values)
    n,s = get_candidate(values)
    print ">> search <<:  cell: (%s) has the  fewest possibilities (%s): " %(n,s)        
    print '>>> Done <<<'