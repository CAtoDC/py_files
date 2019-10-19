# Check for uniqueness between lists

def unique(l):
    if len(l) == len(set(l)):
        print("All elements are unique")
    else:
        print("List has duplicates")

unique([1,2,3,4])   # All elements are unique

unique([1,1,2,3])   # List has duplicates