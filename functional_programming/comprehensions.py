# comprehensions

#comprehensions in lists

my_list = [char for char in 'hello'] #my_list is now ['h','e','l','l','o']
my_list2 = [num**2 for num in range(100)] #my_list2 has my_list2[i] = i*i , i < 100
my_list3 = [num**2 for num in range(100) if num%2 == 0] #my_list3 has all the square of even numbers from 0 to 99

print(my_list)
print(my_list2)
print(my_list3)


#set and dictionary comprehensions

#note that set is similar to lists except for the brackets which will be {} instead of []

my_set = {char for char in 'hello'} #my_list is now ['h','e','l','l','o']
my_set2 = {num**2 for num in range(100)} #my_list2 has my_list2[i] = i*i , i < 100
my_set3 = {num**2 for num in range(100) if num%2 == 0} #my_list3 has all the square of even numbers from 0 to 99

print(my_set)
print(my_set2)
print(my_set3)


#comprehensions in dictionary
simple_dictionary = {
    'a': 1,
    'b': 2
}
my_dict = {key:value**2 for key,value in simple_dictionary.items() if value%2 == 0}

print(my_dict )

your_dict = {key:key*2 for key in range(100)}

print(your_dict)


simple_dictionary = {
    'a': 1,
    'b': 2
}

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n'] #print all the duplicates

duplicates = list(set(item for item in some_list if some_list.count(item) > 1 ))


print(duplicates)
