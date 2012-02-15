'''
recurse test
'''
class Graph(object):
    """
    graph node class definitiion
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
    
def walkpath(dd , dkey, plist=[]):
    """
    Recurse through paths till we reach end    
    """
                                    # end of path?
    print 'process key: %s' %dkey
    if len(dd[dkey]) == 1:
            print 'end of path for %s' %dkey
            return plist
    else:
            v = dd[dkey][0]
            print 'lv: %s' %v
            plist.append(v)
            walkpath(dd,v, plist)
        
#----------------------------------------------------------------------
def walk(g, start, adjlist=[], plist=[]):
    """
    Recursive process over adj nodes
    """
    #if len(adjlist) ==1:
    if len(adjlist) ==0:
            # done 
            #plist.append(adjlist[0])
            print '>>>> walk: done; plist: %s' %plist
            return
    else:
            # iterate/recurse over vertices
            # update path list
            print '>>>> Iterate/Recurse <<<<<'
            plist.append(adjlist[0])
            adjlist.pop(0)
            # find next vertex/node in chain
            nnext = adjlist[0]
            adjlist = g.adj(nnext)
            print 'process next node: %s' %nnext
            walk(g, adjlist, plist)
            
            
def get_path(g, start, end, visited=[]):
    
    # ?All Done?
    if start == end:
        return visited
    else:
        # prevent duplicates
        if start not in visited:
            # process
            #visited = visited + [start]
            visited.append(start)
            # get list of adj nodes
            adjlist = g.adj(start)
            for node in adjlist:
                if end in adjlist:
                # all done
                    return visited
                else:
                    # step to next node in chain and recurse 
                    nextnode = node
                    return get_path(g,nextnode,end,visited)
            
                        
        
if __name__ ==  "__main__":
    # path dict
    pdict ={'a': ['b', 'c'],
    'b':['c'],
    'c':['d']}    

    #rlist = []
    print '>>>> kotest: start <<<<'
    g =  Graph(pdict)
    start = 'a'
    end = 'd'
    
    rlist = get_path(g, start, end)

    print rlist    
    print '>>>> done <<<<'


    # Node list
    #vlist = g.v()	
    #rdict ={}	
    #for node in vlist:
    #        print '>>process node adj list: for vertex: %s; %s'  %(node, g.adj(node))
    #        #rlist =[]
    #        # set start node
    #        #rlist.append(node)
    #        rlist = walk(g,  node)
    #        print rlist
    #        # build  results dict - key is a tuple with start and end nodes
    #        #tpl =(node,rlist[-1])
    #        #rdict[tpl] = rlist
            
    #print '>>>> results : %s' %rdict                        
    #print res




