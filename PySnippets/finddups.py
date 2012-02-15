# find duplicate files - build dict of filenames and path lists

import os
import sys 
import stat # file statistics 
import datetime


# define file types of interest - ignore all others
FTYPES=['py', 'txt']

root= '/home/brencam'
#root= '/home/brencam/code_sandbox/python/MyPythonDev'



def getdata(dictlist, dr, flist):
    '''
    this method gets recursed over - dictlist is passed thru on each call
    '''
    fdict1 = dictlist[0]
    fdict2 = dictlist[1]
    for f in flist:
        # bypass non txt files - get file extension
        ftype = f.split('.')[-1]
        #if not f.endswith('txt'):
        if not ftype in FTYPES:
            continue
        # get file stats
        fullf = os.path.join(dr,f)
        a = []
        fstats = os.stat(fullf)
        fsize = fstats[stat.ST_SIZE]
        a.append(f)
        a.append(str(fsize))
        #print 'fname: %s' %f
        #print 'full path: %s' %fullf
        ## make file name + byte count the dict key
        # this combo defines duplicate files
        dk = ','.join(a)
        if fdict1.has_key(dk):
            # update existing entry
            fdict1[dk] += 1
            fdict2[dk].append(dr)
            # bump duplicate count
            dictlist[2] += 1
        else:
            # create a new entry 
            fdict1[dk] = 1
            fdict2[dk] = []
            fdict2[dk].append(dr)

def process_job(root):
    report = getdata(root)  
    
def report_results(rdictlist):
    '''
    Format o/p report of duplicates in result dictionary
    List name, count + path for each dup found
    '''
    
    rdict = rdictlist[1]
    dupcnt = rdictlist[2]
    print '******* Duplicate File Search Results (from root: %s) ******\n' %root
    
    #print ' Total # of files processed: %s' %len(rdict)   
    #print ' Total # of duplicate files found: %s' %dupcnt
   
    # ?? how to sort dict results ??\
    for items in rdict.iteritems():
        if len(items[1]) == 1:
            # ignore unique entries
            continue
        # report on the dups
        # remove file size from result display
        print '\n Duplicate Filename (dup count: %s ): %s' %((len(items[1]) -1 ),items[0].split(',')[0])
        for item in items[1]:
            print '\t filepath: %s' %item  
            
    print ' Total # of files processed: %s' %len(rdict)   
    print ' Total # of duplicate files found: %s' %dupcnt
            

if __name__ =="__main__":
        
    # print start, end and elapsed times

    dtstart = datetime.datetime.now()
    
    print '\n>>>>Duplicate File Search Starting at: %s <<<<\n' %dtstart.ctime()
    dictlist = []
    fdict1 = {}   
    fdict2 = {}
    dupcnt = 0
    dictlist.append(fdict1)
    dictlist.append(fdict2)
    dictlist.append(dupcnt)
    
    #root= '/home/brencam/code_sandbox/python/MyPythonDev'
    os.path.walk(root, getdata,dictlist) 
    
    #for r, dirs, files in os.walk(root):
    #   print dirs
    #print fdict
    
    # find duplicates
    #for k,v in fdict:
    #dict = dictlist[0]
    
    #for item in fdict2.iteritems():   
        #if len(item[1]) >  1:
            #print '***** Found a Dup: %s; path: %s \n ' %(item[0], item[1])
       
    
    #for item in fdict1.iteritems():        
        #if item[1] > 1:
            #print 'duplicate file found: %s' %item[0] 
            ## get matching list in path dictionary
            #k = item[0]
            #print 'path list: %s'%fdict2[k]
            
    dtend = datetime.datetime.now()        
    elapsed = dtend - dtstart    
    report_results(dictlist)
    
    print '\n>>>>> Ending at: %s <<<<<' %dtend.ctime()
    
    #print '\n >>>> Elapsed Time: <<<<<\n'
    print '>>>>> Total Elapsed Time (in secs): ' + str (elapsed.seconds)
    print '>>>>> Total Elapsed Time (in microsecs): ' + str (elapsed.microseconds)
    
    print '>>>>> Duplicate File Search completed <<<<'


    
 

        

