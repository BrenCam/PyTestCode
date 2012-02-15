
def getdata(fname,count):
    a = ['a','f','g']
    lst = []
    # create list
    textlines = open (fname,'r').readlines()
    lst = map (len(textlines),textlines)
  # for line in textlines:
   #     lst.append ( line)
    #    lst.extend (len(line))
    # convert to a tuple??
    # create tuple of line
    #return textlines
    return lst

    # Sort in ascending order (?how to sort descending)?
    #textlines.sort(key=len)
    #textlines.reverse()
    #textlines.sort (key=len, reverse)
    #for i,line in enumerate(textlines):
        #if i < count:
            #print i,line
    #print 'Finding %s longest lines in file: %s with %s total records:' %( count,  fname, len(textlines))
    #print 'File: %s; Total Rec Count: %s; Line Count: %s ' %(  fname,  len(textlines), count)
    #for x, line in enumerate (reversed (textlines)):
        #if x < count:
            #print len(line), line                        
    #print '>>>> done'   

fname = 'textfile.txt'
count = 3

print '>>>> Begin '   
getdata (fname, count)
#tpl.sort (lambda a,b: a[0]-b[0])
#print tpl
print '>>>> End '   




    
    