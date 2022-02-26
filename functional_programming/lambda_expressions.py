# lambda functions in python

# lambda functions are one-time anonymous functions that we don't need more than once

# because we only use them once, we dont need to name them and store them on our machines and that is why they are anonymous

# lambda param: action(param)
from functools import reduce

my_list = list(range(25))


def multiply_by_2(item):
    return item * 2


print(list(map(multiply_by_2, my_list)))

# above piece of code is same as

print(list(map(lambda item: item * 2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list, 0))

# note that lambda (acc, item) gives a syntax error

# sort the below list based on the second item in each item
my_tuple_list = [(0,2), (4,3), (9,9), (10, -1)]

my_tuple_list.sort(key= lambda x: x[1])
print(my_tuple_list)
