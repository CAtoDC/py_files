# for loop examples

count = 0
friends = ['Joseph', 'Glenn', 'Sally', 'David']
for friend in friends:
    count = count + 1
    print ('Happy New Year', friend,"!")
    print ("I have", count, "friend(s)")
print ("\n")
    
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    # counts number of items in list
    count = count + 1
    print ('Count: ', count)
print ("\n")
 
total = 0
for i in [3, 41, 12, 9, 74, 15]:
    total = total + i
    print ('Total: ', total)
print ("\n")
    

# find the largest value in a set
max_so_far = None
print ('Before:', max_so_far)
for i in [3, 41, 12, 9, 74, 15]:
    if max_so_far is None or i > max_so_far :
        max_so_far = i
        print ('Loop:', i, max_so_far)
        print ('The largest value is:', max_so_far)
        
