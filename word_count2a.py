'''
A python program to count each word in a text file.

It reads through the lines of a file, breaks each line into a list of
words, loops through each of the words in the line, and counts each
word using a dictionary.

Since the Python split function looks for spaces and treats words as
tokens separated by spaces, it will treat the words ``soft!'' and
``soft'' as different words and create a separate dictionary entry for
each word. It does a similar thing with capitalization; it will treat
``who'' and ``Who'' as different words with different counts. 

We can solve both these problems by using the string methods lower, 
punctuation, and translate.

'''
import string

# define punctuation to ignore
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

fname = input('Enter the file name: ')
try:
    my_text_file = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
word_occurrences = {}
line_num = 0
page_num = 0

for line in my_text_file:
    # Syntax:  string.translate(s, table[, deletechars])
    # Delete all characters from s that are in deletechars (if present),
    # and then translate the characters using table, which must be a
    # 256-character string giving the translation for each character
    # value, indexed by its ordinal. If table is None, then only the
    # character deletion step is performed.
    line = line.translate(string.punctuation)
    line = line.lower()
    words = line.split()

    for word in words:
        # get word counts
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
            
        # get word occurrences
        if word_occurrences.has_key(word):
            word_occurrences[word].append(line_num)
        else:
            word_occurrences[word] = [ line_num ]
    
    
# sort words
for key in sorted(counts.iterkeys()):
    print("%s: %s" % (key, counts[key]))

# display unique words
word_keys = word_occurrences.keys()
print("{} unique words found.".format(len(word_keys)))

