def getdata(fname):
    try:
        f = open(fname,'r')
        lst = f.readlines()
        #print lst
        return lst
    except:
        raise "Error - file not found"

def putdata(fname, data):
    f = open(fname, 'w')
    f.writelines(fname, data)

# sort by arbitrary col
def DSU_Sort(lst,col):
    # Move 1st col to front;
    outlst = []
    print lst
    for item in lst:
        sx = '123'
        print 'sx: %s' %sx
        s0 = item.split(' ')
        sortkey = ''.join(s0[col:col+1])
        print 'sortkey: %s' %sortkey
        #print sortkey
        s2 = sortkey.replace('\n',' ')
        print 's2: %s' %s2
        s3 = s2 + item
        s1 = ' '.join(s0[0:col-1])
        #s2 = s1.join(s0[col+1:])
        outlst.append(s3)
    outlst.sort()
    # remove added sort col
    sfinal = []
    for item in outlst:
        s1 = item.split(' ')
        s = ' '.join(s1[1:])
        sfinal.append(s)
    print sfinal
    return sfinal

def parseandsort(lst):
    sout = []
    for item in lst:
        s0 = item.split (' ')
        s1 = ' '.join(s0[1:])
        print s1
        sout.append (s1)
    sout.sort()
    return sout

infile = "zzinfile.txt"
outfile = "zzoutfile.txt"

print '>>> Begin >>>'
inlst = getdata(infile)
#outlst = parseandsort(inlst)
outlst = DSU_Sort(inlst,1)
#print outlst
#outlst = putdata (outfile, outlst)
print '>>> End >>>>'


