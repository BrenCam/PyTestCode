# Simple py recursion test
#

#def recurse(list, total):

def recurse(list, total=0, processed=[]):
    
    #total = total + 0.0 
    # compute total in list
    #rtot = total + 1
    if len(list) ==0:
        print 'bail out: %s' %total
        return total, processed
    else:
        #print 'Add'
        # keep track of processed elements
        processed.append(list[-1])
        #processed = processed + [list[-1]]
        total += list[-1]
        list.pop()
        print 'Adding : rtotal: %s' %total
        # don't forget the return here
        print 'Adding: processed list: %s' %processed
        return recurse(list, total, processed )
        
if __name__ ==  "__main__":

    list =[1,2,3]
    print '>>>> start <<<<'
    inttot = 0
    res,processed = recurse(list)
    print 'Res = %s' %(res) 
    print 'Processed = %s' %(processed) 

    #print res
    #print rlist    
    print '>>>> done <<<<' 
