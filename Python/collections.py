# Collections module provides alternatives to built-in types that can be more efficient or convenient for certain use cases. It includes specialized container datatypes such as namedtuples, deque, Counter, OrderedDict, defaultdict, and ChainMap. These data structures can help improve code readability and performance in various scenarios.

# List
    # Ordererd, Allow duplicates, Mutable
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print("The length of the list is:", len(thislist)) # len() is a built-in function that returns the number of items in an object. When used with a list, it returns the number of elements in that list.
thislist.append("orange") # append() is a built-in method that adds an item to the end of the list. In this case, it adds "orange" to the list.
thislist.remove("banana") # remove() is a built-in method that removes the first occurrence of a specified value from the list. In this case, it removes "banana" from the list.
thislist.pop() # pop() is a built-in method that removes and returns the last item in the list. If an index is specified, it removes and returns the item at that index. In this case, it removes "orange" from the list.
thislist.sort() # sort() is a built-in method that sorts the items of the list in ascending order by default. It modifies the list in place.
thislist.reverse() # reverse() is a built-in method that reverses the order of the items in the list. It modifies the list in place.
thislist.clear() # clear() is a built-in method that removes all items from the list, resulting in an empty list.
thislist.insert(1, "kiwi") # insert() is a built-in method that inserts an item at a specified index in the list. In this case, it inserts "kiwi" at index 1.
thislist.extend(["mango", "grape"]) # extend() is a built-in method that adds all items from an iterable (like another list) to the end of the list. In this case, it adds "mango" and "grape" to the list.
thislist[0] = "pear" # This line modifies the first item in the list (index 0) to be "pear". Lists are mutable, so their elements can be changed.
thislist[1:3] = ["kiwi", "melon"] # This line replaces the items at index 1 and 2 with "kiwi" and "melon". Slicing allows you to modify multiple elements in a list at once.
thislist[1:3] = [] # This line removes the items at index 1 and 2 by assigning an empty list to that slice. It effectively deletes those elements from the list.
thislist = thislist + ["kiwi", "melon"] # This line concatenates the existing list with a new list containing "kiwi" and "melon". The result is a new list that includes all elements from both lists.
thislist *= 2 # This line duplicates the list by repeating its elements twice. The result is a new list that contains two copies of the original list's elements.

print(thislist)
print("The length of the list is:", len(thislist))
print("The first item in the list is:", thislist[0]) # This line prints the first item in the list, which is accessed using index 0.
print("The last item in the list is:", thislist[-1]) # This line prints the last item in the list, which is accessed using index -1 (negative indexing counts from the end of the list).
print("The items in the list from index 1 to 3 are:", thislist[1:4]) # This line prints the items in the list from index 1 to 3 (inclusive of index 1 and exclusive of index 4). Slicing allows you to access a range of elements in a list.
print("The items in the list from index 2 to the end are:", thislist[2:]) # This line prints the items in the list starting from index 2 to the end of the list. Slicing allows you to access a range of elements in a list.
print("The items in the list from the beginning to index 3 are:", thislist[:4]) # This line prints the items in the list from the beginning up to index 3 (exclusive of index 4). Slicing allows you to access a range of elements in a list.
print("The items in the list from index 1 to the end with a step of 2 are:", thislist[1::2]) # This line prints the items in the list starting from index 1 to the end, taking every second item (step of 2). Slicing allows you to access elements at specific intervals.

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist: # This line checks if the string "apple" is present in the list 'thislist'. The 'in' keyword is used to test membership in a sequence (like a list). If "apple" is found in the list, the condition evaluates to True, and the code inside the if block will execute.
  print("Yes, 'apple' is in the fruits list")

# Set
    # Unordered, No duplicates, Mutable, Unchangeable, but can add/remove items

thisset = {"apple", "banana", "cherry"}
print(thisset)

print("The length of the set is:", len(thisset)) # len() is a built-in function that returns the number of items in an object. When used with a set, it returns the number of unique elements in that set.
thisset = {"apple", "banana", "cherry"}

for x in thisset:   # This line starts a for loop that iterates over each element in the set 'thisset'. The variable 'x' will take on the value of each element in the set during each iteration of the loop. Since sets are unordered, the order in which elements are accessed is not guaranteed to be the same as the order in which they were added to the set.
  print(x)

print("banana" in thisset) # This line checks if the string "banana" is present in the set 'thisset'. The 'in' keyword is used to test membership in a collection (like a set). If "banana" is found in the set, the expression evaluates to True; otherwise, it evaluates to False. The result of this check will be printed to the console.
print("banana" not in thisset) # This line checks if the string "banana" is present in the set 'thisset'. The 'not in' keyword is used to test membership in a collection (like a set). If "banana" is found in the set, the expression evaluates to True; otherwise, it evaluates to False. The result of this check will be printed to the console.

thisset.add("orange") # This line adds the string "orange" to the set 'thisset'. The 'add()' method is used to add a single element to a set. If "orange" is already present in the set, it will not be added again, as sets do not allow duplicate elements.
thisset.remove("banana") # This line removes the string "banana" from the set 'thisset'. The 'remove()' method is used to remove a specified element from a set. If "banana" is not present in the set, a KeyError will be raised. If you want to avoid this error, you can use the 'discard()' method instead, which will not raise an error if the element is not found.
thisset.discard("banana") # This line removes the string "banana" from the set 'thisset'. The 'discard()' method is used to remove a specified element from a set. If "banana" is not present in the set, no error will be raised, and the program will continue executing normally. This is different from the 'remove()' method, which raises a KeyError if the element is not found.
thisset.pop() # This line removes the random value from the set 'thisset'.
thisset.clear() # This line removes all the elements from the set 'thisset'.
del thisset # This line will delete the set completely.


tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) # This line updates the set 'thisset' by adding all elements from the set 'tropical'. The 'update()' method is used to add multiple elements to a set. If any of the elements in 'tropical' are already present in 'thisset', they will not be added again, as sets do not allow duplicate elements.
print(thisset)

myList = ["kiwi", "orange"]
thisset.update(myList) # This line updates the set 'thisset' by adding all elements from the list 'myList'. The 'update()' method can accept any iterable (like a list, tuple, or another set) and adds its elements to the set. If any of the elements in 'myList' are already present in 'thisset', they will not be added again, as sets do not allow duplicate elements.
print(thisset)

# Join set 

# union() : Returns a new set with all the items from both the set. set = set1.union(set2) / set = set1 | set2 | set3
# union() can also be used to join set and tuple, union() and update() both will exculde duplicate items.
# insertection() : Returns a new set that contains the items that are present in both the set. set = set1.insetection(set2) / set = set1 & set2
# intersection_update() : Returns only duplicates, but it will change the original set insted of new set.
# difference() : Returns new set that contains only the items from the first set that are not present in the other set. set = set1.difference(set2) / set = set1 - set2
# difference_update() : Returns only the items from the first set that are not present in the other set.
# symmetric_difference() : Returns only the elements that are not present in both set. set = set1/symmetric_difference(set2) / set = set1 ^ set2
# symmetric_difference_update() : Returns all but duplicates, but it will change the original set.

# Frozenset is a immutable version of set.
# Use Frozenset() to create frozenset.

# Methods of Frozenset :
# copy() : returns the copy of set.
# differennce() : returns a new frozenset with a difference.
# intersection() : returns new frozenset with the insersection.
# isdisjoint() : returns true if there is no insersection between two frozenset.
# issubset() : returns true if this frozenset is a subset of another.
# isupperset() : returns true if this frozenset is a superset of aonther.
# symmetric_difference() : returns new frozenset with symmetric difference.
# union() : returns a new frozenset containing the union.

# Dictionary
    # Ordered, No duplicates, Mutable

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict)

print("The length of the dictionary is:", len(thisdict)) # len() is a built-in function that returns the number of items in an object.
# When used with a dictionary, it returns the number of key:value pairs in the dictionary.
print(thisdict["brand"]) # This line accesses the value of the "brand" key using square brackets. In this case, it returns "Ford".
print(thisdict.get("brand")) # get() is a built-in dictionary method that returns the value of a specified key. In this case, it returns "Ford".
print(thisdict.get("model")) # If the specified key does not exist, get() returns None instead of raising an error.
print(thisdict.get("model", "Not Available")) # get() can also accept a default value. If the key does not exist, it returns the specified default value.
thisdict["color"] = "red" # This line adds a new key:value pair to the dictionary. If the key already exists, its value will be changed.
thisdict["year"] = 2025 # This line changes the value of the "year" key from 1964 to 2025. Dictionaries are mutable, so their values can be changed.
thisdict.update({"model": "Mustang"}) # update() is a dictionary method that adds a new key:value pair. If the key already exists, update() changes its value.
thisdict.update({"year": 2026, "electric": True}) # update() can be used to add or change multiple key:value pairs at the same time.
thisdict.pop("electric") # pop() is a dictionary method that removes the specified key:value pair. In this case, it removes the "electric" key and its value.
thisdict.popitem() # popitem() removes and returns the last inserted key:value pair from the dictionary.

del thisdict["year"] # del removes the specified key:value pair from the dictionary. In this case, it removes the "year" key.
thisdict.clear() # clear() removes all key:value pairs from the dictionary. The dictionary still exists, but it becomes empty.
del thisdict # del completely deletes the dictionary.

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict.values()) # values() returns a view containing all the values in the dictionary.
print(thisdict.items()) # items() returns a view containing all the key:value pairs in the dictionary.

if "brand" in thisdict: # This line checks if the "brand" key is present in the dictionary. The "in" keyword is used to test membership.
  print("Yes, 'brand' is present in the dictionary")

if "model" not in thisdict: # This line checks if the "model" key is not present in the dictionary. The "not in" keyword returns True if the specified key is not found.
  print("No, 'model' is not present in the dictionary")

for x in thisdict: # This line starts a for loop that iterates through the dictionary. By default, the loop goes through the keys of the dictionary.
  print(x)

for x in thisdict:
  print(thisdict[x]) # This loop goes through each key and uses the key to access its corresponding value.

for x in thisdict.keys():
  print(x) # keys() explicitly returns all the keys, which can then be accessed using a for loop.

for x in thisdict.values():
  print(x) # values() returns all the values in the dictionary, which can then be accessed using a for loop.

for x, y in thisdict.items():
  print(x, y) # items() returns both the key and value. In this case, x stores the key and y stores the value.

newdict = thisdict.copy() # copy() creates a copy of the dictionary. Changes made to the copied dictionary will not change the original dictionary.
newdict = dict(thisdict) # dict() can also be used to create a copy of an existing dictionary.

thisdict.setdefault("model", "Mustang") # setdefault() returns the value of a key if the key already exists. If the key does not exist, it adds the key with the specified value.

# Dictionary Constructor
thisdict = dict(brand="Ford", electric=False, year=1964) # dict() is a constructor that can be used to create a new dictionary.

# Nested Dictionary
myfamily = {
    "child1": {
        "name": "John",
        "year": 2004
    },
    "child2": {
        "name": "Anna",
        "year": 2007
    }
}

print(myfamily["child1"]["name"]) 
# This line accesses the "name" value inside the "child1" dictionary.
# Dictionaries can contain other dictionaries, which are called nested dictionaries.
# get() : Returns the value of the specified key.
# keys() : Returns a list-like view containing all the keys in the dictionary.
# values() : Returns a list-like view containing all the values in the dictionary.
# items() : Returns a list-like view containing all the key:value pairs in the dictionary.
# update() : Adds new items or changes existing key:value pairs.
# pop() : Removes the item with the specified key.
# popitem() : Removes the last inserted key:value pair.
# clear() : Removes all the items from the dictionary.
# setdefault() : Returns the value of a specified key. If the key does not exist, it adds the key with the specified value.
# fromkeys() : Returns a new dictionary with the specified keys and a specified value.
# Dictionary Comprehension
# Dictionary comprehension is a short way to create a new dictionary based on an existing iterable.
# Example:
thisdict = {x: x * 2 for x in range(5)}
print(thisdict)

# Output:
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Tuple
    # Ordered, Allow duplicates, Immutable, Unchangeable, but can be used to store related pieces of data together

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print("The length of the tuple is:", len(thistuple)) # len() is a built-in function that returns the number of items in an object. When used with a tuple, it returns the number of elements in that tuple.
# tuples are immutable, so they cannot be modified after creation. However, you can access their elements using indexing and slicing, similar to lists.
# tuples can be used to store related pieces of data together, and they are often used for fixed collections of items, such as coordinates or RGB color values.
# tuples can't be created with a single element without a trailing comma. For example, 'single_element_tuple = (5,)' creates a tuple with one element, while 'not_a_tuple = (5)' is just an integer in parentheses.

print("The first item in the tuple is:", thistuple[0]) # This line prints the first item in the tuple, which is accessed using index 0.
print("The last item in the tuple is:", thistuple[-1]) # This line prints the last item in the tuple, which is accessed using index -1 (negative indexing counts from the end of the tuple).
print("The items in the tuple from index 1 to 3 are:", thistuple[1:4]) # This line prints the items in the tuple from index 1 to 3 (inclusive of index 1 and exclusive of index 4). Slicing allows you to access a range of elements in a tuple.
print("The items in the tuple from index 2 to the end are:", thistuple[2:]) # This line prints the items in the tuple starting from index 2 to the end of the tuple. Slicing allows you to access a range of elements in a tuple.
print("The items in the tuple from the beginning to index 3 are:", thistuple[:4]) # This line prints the items in the tuple from the beginning up to index 3 (exclusive of index 4). Slicing allows you to access a range of elements in a tuple.
print("The items in the tuple from index 1 to the end with a step of 2 are:", thistuple[1::2]) # This line prints the items in the tuple starting from index 1 to the end, taking every second item (step of 2). Slicing allows you to access elements at specific intervals.
print("The index of 'banana' in the tuple is:", thistuple.index("banana")) # This line prints the index of the first occurrence of the value "banana" in the tuple. The 'index()' method returns the index of the specified value.
print("The count of 'cherry' in the tuple is:", thistuple.count("cherry")) # This line prints the number of occurrences of the value "cherry" in the tuple. The 'count()' method returns the number of times a specified value appears in the tuple.

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:    # This line checks if the string "apple" is present in the tuple 'thistuple'. The 'in' keyword is used to test membership in a sequence (like a tuple). If "apple" is found in the tuple, the condition evaluates to True, and the code inside the if block will execute.
  print("Yes, 'apple' is in the fruits tuple")

# To update a tuple, you can convert it to a list, modify the list, and then convert it back to a tuple. For example:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple) # Convert the tuple to a list
y[1] = "kiwi" # Modify the list
thistuple = tuple(y) # Convert the list back to a tuple

print(thistuple) # This line prints the updated tuple, which now contains "kiwi" instead of "banana". The output will be: ('apple', 'kiwi', 'cherry')

# To add an item to a tuple, you can convert it to a list, append the item to the list, and then convert it back to a tuple. For example
thislist = ["apple", "banana", "cherry"]
y = list(thistuple) # Convert the tuple to a list
y.append("orange") # Append the new item to the list
thistuple = tuple(y) # Convert the list back to a tuple

print(thistuple) # This line prints the updated tuple, which now contains "orange" as the last item. The output will be: ('apple', 'kiwi', 'cherry', 'orange')

# To remove an item from a tuple, you can convert it to a list, remove the item from the list, and then convert it back to a tuple. For example:
y = list(thistuple) # Convert the tuple to a list
y.remove("kiwi") # Remove the specified item from the list
thistuple = tuple(y) # Convert the list back to a tuple

print(thistuple) # This line prints the updated tuple, which no longer contains "kiwi". The output will be: ('apple', 'cherry', 'orange')
