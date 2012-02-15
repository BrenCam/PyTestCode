def foo(array_input):
	result = []
	for i in range(len(array_input)):
		for j in array_input[i+1:]:
			if j == array_input[i] and j not in result:
				result.append(array_input[i])

	return result

def f1(seq):
	set = {}
	map(set.__setitem__, seq, [])
	return set.keys()
		
artest = [1,2,2,5,6,7,8,6,3,9,9,40,0,0,0,0,3]


import random
import datetime

ar = []
arsize = 4000
for i in range (arsize):
    var = random.randrange(1,arsize)
    ar.append (var)
    #print 'adding random #:' + str(var)

dtstart = datetime.datetime.now()
#print '>>>>>  Test for Array Size = ' + str(arsize)
print '>>>>>  Test for Array Size = ' + str(len(artest))

print '>>>>> Start Time: ' + dtstart.ctime()
#print artest
#print ar
r = foo (ar)
#r = foo(artest)


dtend = datetime.datetime.now()
elapsed = dtend - dtstart
print '>>>>> End Time:  ' + dtend.ctime()
print '>>>>> Total Elapsed Time (in secs): ' + str (elapsed.seconds)
print '>>>>> Total Elapsed Time (in microsecs): ' + str (elapsed.microseconds)
print '>>>>> Duplicate Count: ' + str(len (r))
print '>>>>> Duplicate List: '
print r
print
print '>>>>> Done'
