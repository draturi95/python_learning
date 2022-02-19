myList = list(('hey', 'tiger', 'ass_whooper'))


your_list = [21, 22, 352]

print(myList)
print(len(your_list))

#methods of lists in pythonn
your_list.append('hey') #insert for adding an element
your_list.extend([12, 44,598]) # extend for adding a list
your_list.insert(2, 'jjj')
your_list.reverse()

print(your_list.count('hey'))
print(your_list.index('jjj'))
print(your_list)


#note that .sort() sorts the array  but sorted(array) returns a new array that is sorted. 

