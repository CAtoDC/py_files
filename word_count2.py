'''
Modified for python 3.6

Use: 
./sample_text/Test.txt
./sample_text/AliceInWonderland.txt


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

fname = input('Enter the file name: ')  # text file in same directory

try:
    fhand = open(fname)
except:
    print ('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.translate(string.punctuation)
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

#print (counts)

# sort dict by keys (i.e. words)
# to sort keys in reverse, add reverse=True 
print ('\n')
for key in sorted(counts.keys()):
    print ("%s: %s" % (key, counts[key]))

