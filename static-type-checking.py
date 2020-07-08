from typing import Dict, List, Tuple

'''
Type-checking in python became available with version 3.6  
See:  https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b  
'''


# A function where both parameters are ints
def addition (x: int, y: int):
    return x + y
#print(addition(5,6))


# A dictionary where the keys are strings and the values are ints
name_counts: Dict[str, int] = {
    "Adam": 10,
    "Guido": 12
}
#print(name_counts)


# A list of integers
numbers: List[int] = [1, 2, 3, 4, 5, 6]
#print(numbers)


# A list that holds dicts that each hold a string key / int value
list_of_dicts: List[Dict[str, int]] = [
    {"key1": 1},
    {"key2": 2}
]
#print(list_of_dicts[0])


# Tuples let us create datatypes for each element separately
my_data: Tuple[str, int, float] = ("Adam", 10, 5.7)
#print(my_data[0], my_data[1], my_data[2])

