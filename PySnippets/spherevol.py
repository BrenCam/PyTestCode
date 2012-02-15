def vol(r):
    '''
    The volume of a sphere with radius r is 4/3 π r3. 
    What is the volume of a sphere with radius 5? Hint: 392.6 is wrong!
    '''
    pi = 3.14
    v = (r*r*r) *4/3 * pi
    return v


def print_spam():
    print 'spam'
    return

def repeat(fn):
    print '*** repeat ***'    
    fn()
    fn()
    return

r = 5

res = vol(r)

print '>>>> Start <<<<<'

#print 'Sphere Vol: %s' %res

repeat(print_spam)


print '>>>> End <<<<<'
    