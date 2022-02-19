# == vs is in python 

# == checks if two values are equal by converting them to same type  but is checks if the two values are exactly same, for lists, dicts, tuples, set it also checks if they are in same place in memory


#for loop in python

for elt in [1,2,3,4,5]: 
  print(elt)
print(elt, 'the elt stores the value still!')

for num in [1,2,3,4,5]: 
  for alph in {'a','b','c','d','e'}: 
    print(num, alph)


# iterable is an object (set, list, dictionary, tuple) that can be inerated/ looped over. 

#iterating over objects in python 

user = {
  "name": 'Golem', 
  'age': 6501, 
  "occupation": 'wizard'
}

for item in user: #note that in prints index 
  print(item) 

for item in user.items(): # .items() property lets us access each key value pair
  print(item)

for item in user.values(): 
  print(item)

for item in user.keys():
  print(item)

for item in user.items(): 
  key, value = item  # note that we can destructure in python as well like this 
  print(key, value)

for key, value in user.items(): 
  print(key, value)

for num in range(10): 
  print(num)

for num in range(10, 0, -2):
  print(num)

for num in range(2): 
  print(list(range(0,15)))