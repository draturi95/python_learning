# Method Resolution Order

# the mro order can be checked through the method .mro()

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)

print(D.mro())

print(D.__mro__)


# MRO basically tells the order in which python looks for a method/attribute through parent classes
# Python first checks for the method in the class, then all the parent classes in order of inheritance(B and then C),
# #then all the parent's parent classes in order of inheritance and so on untill it either finds the said method/attribute
# or doesnt find it even up in the object base class