#Sets - unordered collections of unordered objects 
#note that in python every data type is an object 

#note that we use 'in' keyword to check if something is in lists, tuples, sets or dictionaries 


my_set = {1,2,3,4,5,6,6,6,5} # note that only unique values will be stored and the duplicates wont be 
#note that set objects dont support indexing i.e. set[0], set[1]...

print(my_set)

your_set = set(('aa', 'bb', 'bb', 'cc'))

print(your_set)

#set methods 

my_set.add(33)

my_set2 =  my_set.copy()

print(my_set)


#my_set.clear() just as in lists, dicts, set also have clear() method

#difference()

set1 = {1,2,3,4,5}
set2 =  {4,5,6,7,8,9}


print(set1.difference(set2)) #this will do exactly what we read in maths that A-B is A without the intersection of A and B sets

#set1.discard() removes the given elt from set if it is in the set

set1.discard(2)
set1.discard(25)
print(set1)

#difference_update does the same thing as difference() but difference_update updates the set and the difference() returns a new set

set1.difference_update(set2)
print(set1)

#set1.isdisjoined(set2) returns True if set1 and set2 are disjoint else it returns False 

#myset.union(your_set) returns  a mathematically literal union of both sets 

#set1.intersection(your_set) returns a mathematically literal intersection of both sets

#myset.issubset(yourset) returns True if myset is subset of yourset

#myset.issuperset(yoruset) returns True if myset is superset of yourset 
