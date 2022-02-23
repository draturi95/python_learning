# Dunder Methods in Python - Finally!
# note that dunder methods in python are special methods with (double under score) and they are used to implement functions like len()

# usually we shouldnt overwrite dunder methods but we have the power to do so

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return ('I see {}'.format(self.color))

    def __len__(self):
        return 5

    def __del__(self):
        print('Deleted!')

    def __call__(self):  # call function basically lets us call the class instance as a method
        return 'yesss?'

    def __getitem__(self, key):
        return self.my_dict[key]


action_figure = Toy('red', 0)

# note that action_figure.__str__() is same as str(action_figure)

print(action_figure.__str__())

print(str(action_figure))

# note that we can change the __str__() functions in the class and then str() method will also change as python methods like  str come from this dunder methods

# note that usually we cant modify dunder methods but sometimes there are special cases


# note that str() has only changed for the toy class. It will still work perfectly for other objects like below

print(str(45))

print(len(action_figure))  # prints 5
print(len('hey hey mama'))  # returns 12

# similarly as str, len is only modified for the toy class and will work in its default state for other objects

# del action_figure

print(action_figure())

print(action_figure['name'])

# note that the __getitem__ dunder is used only with indexed objects like arrays, typles and dictionaries and it helps in accessing these objects   so these attributes can only
# be modified by their own instances and thus implements abstraction.
#action_figure['name'] = 'comic' this would give error as Toy' object does not support item assignment as getitem doesnt
# let you modify and only access the my_dict dictionary
