
def find_path(dd, start, end, visited=[]):
    """
    build a list of nodes between start and end
    return values: node list or None if no path found
    
    """

    assert isinstance (dd,dict)
    
    print '>>> Calling find_path; visited: %s <<<' %visited
    if start == end:
        print '>>>> Done: returning visited: %s' %visited
        return visited
    
    # list of adjacent nodes
    adjlist = dd[start]
    if end not in adjlist:
        # mark path as visited
        visited.append(start)  
        print 'Iterating: Node: %s; Adjlist: %s' %(start, adjlist)
        for node in adjlist:
            if not node in visited:    
                newpath = find_path(dd, node, end, visited)
                # keep searching unless we've been here before
                print 'returning new path: %s' %newpath
                return newpath
            else:
                print 'returning none'
                return None
    

if __name__ ==  "__main__":
    
    import os
    # path dict
    pdict ={'a': ['b', 'c'],
    'b':['c'],
    'c':['d']}    
    
    #rlist = []
    fname = os.path.dirname(__file__)
    
    print '>>>> start - process file: %s <<<<' %fname

    start = 'a'
    end = 'd'
    mypath = find_path(pdict, start, end)
        
    print '>>>> path: %s' %mypath
                
    #print res
    #print rlist    
    print '>>>> done <<<<'