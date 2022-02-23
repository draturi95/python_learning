# this is the coolest thing I have ever found in python!!
# we can inherit classes like list, tuples, dictionaries and use their methods in our class

class SuperList(list):
    def print(self):
        print(self)

    def __len__(self):
        return 1000


super_list1 = SuperList()

super_list1.append('hey')

super_list1.print()
print(super_list1[0])
print(len(super_list1))

print(issubclass(SuperList, list))
print(issubclass(list, object))