#note that in python we dont have null, instead we have NotImplemented
#dictionary in python 

data = dict({'day': "2022 Feb 14 Mon", "season": 'Winter'})
print(data)
user = {
  'name': 'East', 
  'place': 'London'
}

# to check if a dictionary has a key, we do 
print(user.get('score'))

print(user.items()) # returns key, value as a tuple 

#.keys() and .values() for keys and values of a dictionary respectively

#.pop_item() will remove the last added key-value pair 

#pop() will remove the item with the given key

#.update() updates the dictionary with the given key value pair, if the pair doesnt exit, it will be added

user.update({'name': 'Phenom', 'Height': '5Eleven'})

print(user)

#.setdefault() returns the value of the specified key, if the key doesnt exists, inserts the key with the specified key

print(user.setdefault('named', 'Python'))


print(user.get('number', 976)) 
#above note that if number is not a property, 976 is returned else if it is , user['number'] is returned

#1
dictionary = {
  'name': 'Dhawal',
  "age": 23, 
  'favourite_numbers': [1, 2,3,4, 5],
  12: 'euuuu'
}

print(dictionary['name'])

#Note that in python, the keys can only be types that cant be changed i.e. immutable, like strings, numbers, booleans, tuples but not a list 