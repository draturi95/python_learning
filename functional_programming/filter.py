#filter in python

my_list = list(range(25))

def check_if_odd(item):
    return True if (item%2) else False

print(list(filter(check_if_odd, my_list)))
print(my_list)#unchanged

my_odd_list = list(filter(check_if_odd, my_list))

print(my_odd_list)