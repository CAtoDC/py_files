'''A set is a list with no repeated values'''

my_set = {'private student loan', 'credit report', 'loan', 'report', 'regulatory', 'continuity', 
'collection', 'credit report', 'prudent', 'loan', 'report', 'delay', 'consumer', 'deceptive', 'unfair', 
'PPP', 'safety and soundness', 'mortgage', 'foreclosure', 'eviction', 'consumer', 'report', 'regulatory', 
'consumer', 'mortgage', 'safety and soundness', 'loan', 'regulatory', 'mortgage', 'report', 'consumer', 
'regulation', 'eviction', 'moratorium', 'consumer', 'mortgage', 'foreclosure', 'eviction', 'moratorium', 'credit report', 'report', 
'consumer', 'mortgage', 'safety and soundness', 'safe and sound', 'regulation', 'consumer', 'mortgage', 'prudent', 'loan', 
'consumer', 'mortgage', 'regulation', 'consumer', 'foreclosure', 'eviction', 'rule', 'consumer', 'prudent', 'loan', 
'mortgage', 'foreclosure', 'eviction', 'loan', 'report', 'examination', 'exam', 'loan', 'foreclosure', 'eviction', 
'examination', 'exam', 'regulatory', 'continuity', 'mortgage', 'supervision', 'safety and soundness', 'deposit', 'loan', 
'prudent', 'loan', 'report'
}

for i in my_set:
    print (i)

with open('tags.txt', 'w') as filehandle:
    for listitem in my_set:
        filehandle.write('%s\n' % listitem)
