#!/usr/bin/python
# code to find shortest string entry in a dictionary with a length > 1
# experiments with map, zip, reduce and filter

ta_dict = {}
ta_dict['A'] = '135'
ta_dict['B'] = '2379'
ta_dict['C'] = '89'
ta_dict['D'] = '36789'
ta_dict['E'] = '3'
# to convert items from a dictionary first:

#ta_items = [(v, k) for k, v in ta_dict.iteritems()]
ta_items = [v for v in ta_dict.itervalues()]

#ta_items = ['123', '2379', '89', '3']
ta_len = map (lambda x: len(x), ta_items)
ta_zip = zip(ta_len, ta_items)
ta_filtered= filter (lambda x:x[0] >1, ta_zip)
# how to filter this result ??
ta_filtered.sort()

el = ta_filtered[0]

print "Next candidate is: %s; possible values: %s" %(el[0], el[1])


        
    