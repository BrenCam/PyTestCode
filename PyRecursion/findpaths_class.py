'''
Find paths in a graph - see: http://www.python.org/doc/essays/graphs/
'''
    
class Graph(object):
    """
    graph node definitiion
    """
    def __init__(self,g):
            """Constructor"""
            self.g = g
            return
    
    def  v(self ):
            """ list of vertices"""
            return  self.g.keys()
    
    def  adj(self, k): 
            """adjacency list"""
            return self.g[k]


# small graph
grph1 ={'a': ['b', 'c'],
        'b':['d'],
        'c':['d']}

# more complex graph
grph2 = {'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']}



def find_all_paths(graph, start, end, path=[]):
    '''
    Find all available paths
    '''
    
    print '>>>> Process Current (Start/End/Path) Nodes: %s; %s; %s' %(start, end, path)
    # make a new list here - append will not work
    path = path + [start]
    #path.append(start)
    if start==end:
        # return as a list
        print '>>>> return path: %s <<<<' %path
        return [path]
    
    if not start in graph.keys():
        return None

    #    
    # modify to find additional paths
    #
    paths = []
    for node in graph[start]:
        if node not in path:
            # search from new starting point
            print '>>>> nested call - current node: path: %s; %s <<<<' %(node,path)
            nps = find_all_paths (graph, node, end, path)
            if nps is None:
                return None
            for np in nps:
                paths.append(np)

    print '**** return paths: %s ' %paths                
    return paths

def find_path(gc, start, end, path=[]):
    '''
    Finds first available path
    '''

    # create new list
    print '>>>> Process Current (Start) Node: %s' %start 
    path = path + [start]    
    if start==end:    
        return path
    
    if not start in gc.v():
        return None
    
    for node in gc.adj(start):
        if node not in path:
            # search from new starting point
            newpath = find_path (gc, node, end, path)
            if newpath: return newpath          
    return None

if __name__ ==  "__main__":
    
    #rlist = []
    print '>>>> start <<<<'
    
    # use graph class    
    gc = Graph(grph1)
       
    res = find_path(gc, "a", "d")
    print ' first path: %s' %res

    #res = find_all_paths(grph1, "a", "d")
    #if res is None:
    #    print '>>> No path found <<<<'
    #else:
    #    for path in res:            
    #        print '>> found paths: %s' %path
 
    print '>>>> done <<<<'
          