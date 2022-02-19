#enumerate() adds a counter to an iterable and returns a enumerable object

for i, char in enumerate('Helloooo there'): 
  print(i, char)

#note that using a list() outside of enumerate will return an array of key, value pairs as tuples 
for item in [1,2]: 
  print(list(enumerate('risk')))


for i, char in enumerate(list(range(10))): 
  print(list((i, char)))

