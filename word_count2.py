'''
A Python program to count each word in a text file.
It reads through the lines of a file, breaks each line into a list of
words, loops through each of the words in the line, and counts each
word using a dictionary.

We have two 'for' loops. The outer loop is reading
the lines of the file and the inner loop is iterating through each of
the words on that particular line. Because the inner loop executes all
of its iterations each time the outer loop makes a single iteration,
we think of the inner loop as iterating ``more quickly'' and the outer
loop as iterating more slowly. The combination of the two nested loops
ensures that we will count every word on every line of the input file.

Since the Python split function looks for spaces and treats words as
tokens separated by spaces, we would treat the words ``soft!'' and
``soft'' as different words and create a separate dictionary entry for
each word. Also since the file has capitalization, we would treat
``who'' and ``Who'' as different words with different counts. We can
solve both these problems by using the string methods lower, punctuation,
and translate.

'''
import string

# define punctuation to ignore
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print ('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    # Syntax:  string.translate(s, table[, deletechars])
    # Delete all characters from s that are in deletechars (if present),
    # and then translate the characters using table, which must be a
    # 256-character string giving the translation for each character
    # value, indexed by its ordinal. If table is None, then only the
    # character deletion step is performed.
    line = line.translate(None, string.punctuation)
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# sort dict by keys
# to sort keys in reverse, add reverse=True as second keyword argument
# to sorted function
print ('\n')
for key in sorted(counts.iterkeys()):
    print ("%s: %s" % (key, counts[key]))

#print counts
