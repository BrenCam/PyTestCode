'''
    Thinking Python - Ex 12.3;
   Anagram Processor - find a list of anagrams in a word list
   Build a dictionary keyed by character string + word list
'''

def builddict(wordlist):
    #build key from asc order of chars
    mydict = {}
    for item in wordlist:
        #print 'item: %s' %item
        chrlst = list(item)
        chrlst.sort()
        chrkey = ''.join(chrlst)
        #print 'dictkey: %s ' %chrkey
        if not chrkey in mydict:
            mydict[chrkey] = [item]
            #mydict[chrkey] = item
        else:
            #mydict[chrkey] += ', ' + item
            mydict[chrkey].append(item)
    return mydict

def freqsort(d):
    ''' Sort dictionary by frequency '''
    l = []
    for v in d.values():
        if len(v)> 0:
            # append a tuple
            l.append((len(v),v))
    l.sort()
    l.reverse()
    return l

wlist = 'deltas','desalt','midget', 'slated', 'staled', 'moon', 'mono'
print '>>> Start '
mydict = builddict(wlist)
print '>>> Dictionary result:'
print mydict.items()
#print mydict.keys()
#print mydict.values()

keylst = mydict.keys()
keylst.sort()
for item in keylst:
    wlist = mydict[item]
    #l = wlist.split(',')

    # count # of items in list
    #l = wlist.split(',')
    #print len(wlist)
    print 'character list: %s; anagrams: %s; item count: %s' %(item, wlist, len(wlist))

l = freqsort(mydict)
print '>>>> Results in Frequency Order:'
for item in l:
    print item

print '>>> End <<<'





