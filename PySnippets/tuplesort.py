# Count characters in a string into a list of (char, frequency) tuples
# Sort the list of tuples by char and by frequency
# Tested with Python version 2.4 by    Ene Uran   10/05/2006

str1 = 'mississippi mudslide'
dict1 = {}
for k in str1:
    dict1[k] = dict1.get(k, 0) + 1

letter_frequency = dict1.items()
print letter_frequency  # [(' ', 1), ('e', 1), ('d', 2), ('i', 5), ('m', 2), ('l', 1), ('p', 2), ('s', 5), ('u', 1)]

# inplace sort by item at index=0 (default) of tuple (i.e. character)
letter_frequency.sort()
print letter_frequency  # [(' ', 1), ('d', 2), ('e', 1), ('i', 5), ('l', 1), ('m', 2), ('p', 2), ('s', 5), ('u', 1)]

# inplace sort by item at index=1 of tuple (i.e. frequency), highest frequency first (--> reverse)
import operator
index1 = operator.itemgetter(1)
letter_frequency.sort(key=index1, reverse=True)
print letter_frequency  # [('i', 5), ('s', 5), ('d', 2), ('m', 2), ('p', 2), (' ', 1), ('e', 1), ('l', 1), ('u', 1)]

print "-"*45  # line of 45 dashes

# for improved display of the result ...
print "Original string:", str1
print "-"*45
print "Character and frequency:"
for item in letter_frequency:
    if item[0] == " ":
        note = "(space)"
    else:
        note = ""
    print "%s  %d %s" % (item[0], item[1], note)