some_list = ['a', 'b', 'c', 'b', 'd','m', 'n', 'n']

#best solution for python 

duplicates = []
for alph in some_list: 
  if(some_list.count(alph) > 1):
    if alph not in duplicates: 
      duplicates.append(alph)

print(duplicates, 'these are the duplicates baby')

#other solutions below 

alph_tracker = [0]*26

for alph in some_list:  
  index = ord(alph) -ord('a')
  alph_tracker[index] += 1 

print(alph_tracker)

for index in range(0,26): 
  if alph_tracker[index] > 0: 
    print(chr(index + ord('a')))

for alph in some_list: 
  index = ord(alph) - ord('a') 
  if(alph_tracker[index] > 0): 
    print(alph)
    alph_tracker[index] = 0
  

