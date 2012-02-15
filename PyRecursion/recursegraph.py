'''
recurse test
'''
# path dict
pdict ={'a': ['b', 'c'],
        'b':['c'],
        'c':['d']}

class graph(object):
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

		#----------------------------------------------------------------------
	def  adj(self, k): 
		"""adjacency list"""
		return self.g[k]

#----------------------------------------------------------------------
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
def walk(g,  adjlist=[], plist=[]):
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
		
if __name__ ==  "__main__":

	#rlist = []
	print '>>>> start <<<<'
	g =  graph(pdict)
	vlist = g.v()	
	rdict ={}	
	for node in vlist:
		print '>>process node adj list: for vertex: %s; %s'  %(node, g.adj(node))
		rlist =[]
		# set start node
		rlist.append(node)
		walk(g,  g.adj(node), rlist)
		print rlist
		# build  results dict - key is a tuple with start and end nodes
		tpl =(node,rlist[-1])
		rdict[tpl] = rlist
		
	print '>>>> results : %s' %rdict
				
	#print res
	#print rlist    
	print '>>>> done <<<<'




