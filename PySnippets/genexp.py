#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Some simple generators can be coded succinctly as expressions using a 
syntax similar to list comprehensions but with parentheses instead of brackets.
These expressions are designed for situations where the generator is used
right away by an enclosing function. Generator expressions are more compact
but less versatile than full generator definitions and tend to be more memory 
friendly than equivalent list comprehensions.'''


def fact(n):
    # recursive factorial routine
    if n == 1:
        return 1
    else:
        while n > 0:
            return n * fact(n-1)

n = 5        
r = fact(n)
print r

# non recursive equivalent
def nrfact(n):

    prod = 1
    for i in range(1,n+1):
        prod = prod * i
    return prod
    

n = 5        
r = nrfact(n)
print r

#def rfact(n):
    #return n*n-1

    
#def factn(n1):
#    totl = sum (i 
#print fact(3)

#totl =(sum(rfact(i) for i in range(5)))
#ll = list(totl)
#print totl

xvec = [10, 20, 30]

yvec = [7, 5, 3]


sum(x*y for x,y in zip(xvec, yvec))         # dot product

from math import pi, sin
sine_table = dict((x, sin(x*pi/180)) for x in range(0, 91))


#unique_words = set(word  for line in page  for word in line.split())


#valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf' 
l = list(data[i] for i in range(len(data)-1,-1,-1))
print l
#['f', 'l', 'o', 'g']


