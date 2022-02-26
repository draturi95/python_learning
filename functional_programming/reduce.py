# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print#reduce in python

#doesnt come in python built-in functions so we need to import a module for it. Here, we do it as below
from functools import reduce

my_first_list = [1,2,3]

def accumulator_func(accumulator, item):
    return accumulator + item

print(reduce(accumulator_func, my_first_list, 0))


#syntax : reduce(accumulator_function, iterable_item, accumulator_initial_Value)

#Note that the return value from the accumulator function becomes the value of the accumulator in the next call and so on.
#so above, accumlator:  0 (initial), item: 1
#then accumulator: 1, item: 2
#then accumulator: 3, item: 3
#finally accumulator is returned which is 6

