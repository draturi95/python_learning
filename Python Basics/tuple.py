#tuples 

#tuples are basically lists that are immutable. 
#note that lists were mutable i.e. it / it's elements could be assigned other values in python but tuples are not


a,b,c,*other,d = (1,2,3,4,5,6,7,8); 
print(other)

my_tuple  = (1,2,4,5,6,78)

#count() - returns the number of times a value occurs 
#index () - returns the first index of value that is provided to it 
#len(tuple) returns the length of tuple 

#my_tuple[2] = 4 will give error as you cannot assign values to indexes of a tuple

print(my_tuple[3])
print(my_tuple)

tuple_other = tuple(('hey', 'baby'))
print(tuple_other[0:2])
#note that tuple with single item must be written with , after elt otherwise python doesnt recognise it as tuple 

your_tuple  = (273,)