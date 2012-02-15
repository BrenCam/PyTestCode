#!/usr/bin/python

# code to find shortest string entry in a dictionary with a length > 1
# experiments with map, zip, reduce and filter

def find_shortest_string_in_dict(d):
    # get value using list comprehension + generator expression
    # l = length, k = key, v = value
    l,k = min((len(d[s]),s) for s in d if len(d[s]) > 1)
    # get dict key value
    v = d[k]
    return k,v,l

# Test Dict
d = {}
d['A'] = '135'
d['B'] = '2379'
d['C'] = '89'
d['D'] = '36789'
d['E'] = '3'

key,value,length =find_shortest_string_in_dict(d)

minval = min((len(d[s])) for s in d if len(d[s]) > 1)


k = min_item[1]
l = min_item[0]
v = d[k]
#print min_item

print "Shorttest dictitem with length > 1: key: %s; value length: %s, value: %s  " %(k,l,v)

#m = max(d.iteritems(),key = lambda x:x[1])

#m = max([d([x],x) for x in d])[1]
#  d.values(
#e =d.values().sort(cmp=lambda a,b:cmp(d[a],d[b]))

#print e

# print the dict
# using iteration
#
minlen = 9
minitem = ""
for item in d.iteritems():
    print "Key: %s; Value: %s, Len: %s " %(item[0], item[1], len(item[1]))
    ilen = len(item[1])
    if ilen> 1:
        if ilen < minlen:
            minlen = ilen
            minitem = item[1]
            
            
            
# Convert dict to list; then filter and reduce?

            
print "Shortest Entry is : %s; len: %s" %(minitem, minlen)


a =[5,1,4,66,77]
aa = ['123', '2379', '89', '3'] 

b = filter(lambda x: x>1, a)

print b

bb = filter(lambda x: len(x)>1, aa)
print bb

def  mval(x,y):
    return min(x,y)


m = reduce(mval, b)

mm = reduce(mval, filter(lambda x: x>1, a))
print "minval: %s" %mm


# filter array and reduce to shortest element in an array
testarray = ['123', '2379', '89', '3']

ta_dict = {}
d['A'] = '135'
d['B'] = '2379'
d['C'] = '89'
d['D'] = '36789'
d['E'] = '3'
# to convert items from a dictionary first:

ta_items = ['123', '2379', '89', '3']
ta_len = map (lambda x: len(x), ta_items)
ta_zip = zip(ta_len, ta_items)
ta_filtered= filter (lambda x:x[0] >1, ta_zip)
# how to filter this result ??
ta_filtered.sort()

el = ta_filtered[0]

print "Next candidate is: %s; possible values: %s" %(el[0], el[1])

print ">>> Done <<<"

def  mstr(x,y):
    l1 = len(x)
    l2 = len(y)
    return min(l1,l2)

ff = filter(lambda x: len(x)>1, testarray)
#mmm = reduce(mstr, filter(lambda x: len(x)>1, testarray))
#mmm = reduce(mstr, ff)

#print "minval: %s" %mmm

# lambda approach ?

ll = map(lambda item:[len(item[1]),item[0]], d.items())
ll.sort()

print ll[0]

# ??More efficient ??
mmin = min(d, key = lambda x: len(d.get(x)))

# Using List Comprehensions (easier)
min((len(d[s]),s) for s in d if len(d[s]) > 1)

#print filter(lambda x: len(x) > 1, lst)

#print d.iteritems(),x for x in d
        
    