# very efficient way to get word and word length

my_file = 'c:/py/sample_text/LoremIpsum_05.txt'

word_and_len = map(lambda word: (word, len(word)), open(my_file,"r").readline().split())
print (word_and_len)
