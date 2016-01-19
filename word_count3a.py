'''
A python program to count each word in a text file.

It reads through the lines of a file, breaks each line into a list of
words, loops through each of the words in the line, and counts each
word using a dictionary.

Since the Python split function looks for spaces and treats words as
tokens separated by spaces, it will treat the words ``soft!'' and
``soft'' as different words and create a separate dictionary entry for
each word. It does a similar thing with capitalization. It will treat
``who'' and ``Who'' as different words with different counts. 

We can solve both these problems by using the string methods lower, 
punctuation, and translate.

'''
import string

# define punctuation to ignore
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

fname = raw_input('Enter the file name: ')
try:
    my_text_file = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()


counts = dict()
word_occurrences = {}
line_num = 0
page = 1


for line in my_text_file:
    # Syntax:  string.translate(s, table[, deletechars])
    # Delete all characters from s that are in deletechars (if present),
    # and then translate the characters using table, which must be a
    # 256-character string giving the translation for each character
    # value, indexed by its ordinal. If table is None, then only the
    # character deletion step is performed.
    line = line.translate(None, string.punctuation)
    line = line.lower()
    # is this doing anything?
    line_num = line_num + 1
    #char_count = str.count(line,0, 80)
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
            
        # page break
        # assumes 28 lines of text to a page
        if line_num > 61:
            page = page + 1
            line_num = 0 
            
    
# sort words
for key in sorted(counts.iterkeys()):
    print "%s: %s" % (key, counts[key])
    
# display 
print '\n'
if page > 1:
    print "There are %s pages. The last line number is %d." % (page, line_num)
print "There is %s page. The last line number is %d." % (page, line_num)

# display unique words
word_keys = word_occurrences.keys()
print "{} unique words found.".format(len(word_keys))

