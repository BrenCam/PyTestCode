#!/usr/bin/python

def find_shortest_string_in_dict(d):    
    # find shortest string entry in a dictionary with a length > 1
    # note: this solution uses list comprehension + generator expression
    #  "(len(d[s]),s)" <----- outer parenthesis here denotes 
    # that this is the generator expression  
    
    # l = length, k = key, v = value
    l,k = min((len(d[s]),s) for s in d if len(d[s]) > 1)
    # get dict key value
    v = d[k]
    return k,v,l

def test():
    # Test Dictionary
    d = {'A':'135', 'B':'2379','C': '89', 'D': '36789','E':'3'}
    key,value,length = find_shortest_string_in_dict(d)  
    assert key == 'C'
    assert value == '89'
    assert length == 2
    print "Shorttest dictitem with length > 1: key: %s; value length: %s, value: %s  " %(key,length, value)
    print ">>>> All tests passed <<<<"
       
if __name__ == '__main__':
    test()








        
    