#Here\u2019s an example that uses do_twice to call a function named print_spam twice.

def print_spam(val):
    print '**** Value: %s ****' %val
    return
    
'''
do_twice(print_spam)
1. Type this example into a script and test it.
2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
function twice, passing the value as an argument.
3. Write a more general version of print_spam, called print_twice, that takes a string as a
parameter and prints it twice.
4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
argument.
5. Define a new function called do_four that takes a function object and a value and calls the
function four times, passing the value as a parameter. There should be only two statements in
the body of this function, not four.
You can see my solution at thinkpython.com/code/do_four.py.

'''

def do_twice(print_fn, val):
    #print 'do_twice'
    print_fn(val)
    print_fn(val)
    return

def do_four(fn, val):
    print '>>>> do_four <<<<'
    do_twice(fn, val)
    do_twice(fn, val)
    return
    


if __name__ == '__main__':
    
    print '>>> Start <<<<'
    
    #do_twice(print_spam, '\n spam, spam ...')
    do_four(print_spam, 'spam, spam, spam, spam ...')
    
    print '>>> End <<<<'
