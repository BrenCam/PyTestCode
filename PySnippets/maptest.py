import operator

def fnlen(line):
    return  line + ',' + str( len (line))

def mult (x):
    return x*x

print '>>>> Maptest Begin: '   
a =['123', 'x', 'pp33', 'qaerty567', 'arerwuierwru']
b = [3,4,5]
#lst = map (mult, b)
lst = map (fnlen,a)

#sort returned list - sort by len
#lst.sort(key=operator.itemgetter(2))
lst.sort(key= lambda i:i[2])
count =2
for x, line in enumerate (reversed (lst)):
    if x < count:
        #clean up line len
        y=line.split(',')
        #print len(line), line.split(',')                        
        print len(line), y[0]                        
print lst
print '>>>> Maptest End: '   
