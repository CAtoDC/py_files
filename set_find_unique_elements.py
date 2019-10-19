# Another SET example

my_string = "aavvcczcddddeee"

# converting the string to a set
temp_set = set(my_string)

# stitching set into a string using join
new_string = ''.join(temp_set)

print(new_string)

# OUTPUT (not in any particular order by default)
# acedvz

print(sorted(new_string))

# OUTPUT (a list)
# ['a', 'c', 'd', 'e', 'v', 'z']