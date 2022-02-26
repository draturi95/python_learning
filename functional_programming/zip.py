#zip in python

#takes two or more iterables (lists, tuples, dicts etc) as parameters and zips them one at a time from each into a tuple
# eg: [1,2,3] and [4,5,6] into [(1,4), (2,5), (3,6)]
# if sizes of lists are unequal, the tuples are made till the smaller of the two lengths

my_first_list = [1,2,3]
my_second_list = [9,5,5]
my_third_list = [5,7,8,9,5]

print(list(zip(my_first_list, my_second_list)))


print(list(zip(my_first_list, my_third_list)))

print(list(zip(my_first_list, my_second_list, my_third_list))) #[(1, 9, 5), (2, 5, 7), (3, 5, 8)]
