def find_path(dd, start, end, visited=[]):
    """
    build a list of nodes between start and end
    return values: node list or None if no path found
    """
    assert isinstance (dd,dict)
    # update visited path on every request
    #visited.append(start)   
    
    
    # Create a new list here - we don't want to append to any previous path
    # using #visited.append(start) will cause problems
    visited = visited + [start]   
    
    print '>>> Calling find_path; visited: %s <<<' %visited
    if start == end:
        print '>>>> Done: returning visited: %s' %visited
        return visited
    
    # verify start node exists - else fail search and bail out
    if not start in dd.keys():
        print '******* No Available Path Found ******'
        return None
    
    #get list of adjacent nodes and iterate/recurse over each
    adjlist = dd[start]
    print 'Iterating: Node: %s; Adjlist: %s' %(start, adjlist)
    #for node in adjlist:
    for node in dd[start]:
        
        # ?? handle backtracking ??
        print 'Current Node: %s; Visited: %s' %(node, visited)
        if node not in visited:    
            newpath = find_path(dd, node, end, visited)
            # keep searching unless we've been here before
            if newpath:                 
                print 'returning new path: %s' %newpath                
                return newpath 
    # fail - we get here if no path found
    print '>>>> No path found <<<<' 
    return None
        
if __name__ ==  "__main__":
    
    import os
    # path dict - simple
    pdicts ={'a': ['b', 'c'],
    'b':['d'],
    'c':['d']}   
   
    # more complex graph
    pdictc = {'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['E'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']}   
         
    fname = os.path.dirname(__file__)    
    print '>>>> start - processing file: %s <<<<\n' %fname
    start = 'a'
    end = 'd'
    # simple case
    mypath = find_path(pdicts, start, end)
    print '\n>>>> pdicts test - computed path from: %s to %s: %s\n' %(start, end, mypath)

    start = 'A'
    end = 'F'

    mypathc = find_path(pdictc, start, end)
    print '\n>>>> pdictc test - computed path from: %s to %s: %s\n' %(start, end, mypathc)

    print '\n>>>> done - processing file: %s <<<<' %fname
