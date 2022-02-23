# map in python

my_list = [1,2,3,4]
def multiply_by_2(item):
    return item*2

print(list(map(multiply_by_2, my_list)))

print(my_list) # note that just like Javascript, python doesnt change my_list either.
my_two_list = list(map(multiply_by_2, my_list))

print(my_two_list)