# we can check if an instant is of some class by using isinstance(object, class) like below

class User:
    def __init__ (self, name):
        self.name = name

    def human_introduction(self):
        print('hey there I am {self.name}'.format(self.name))


class Wizard(User):
    def __init__(self, name, power, no_of_lives):
        super().__init__(name)
        self.power = power
        self.no_of_lives = no_of_lives

    def wizard_introduction(self):
        print("hey broda! I'm the awesome wizard {}. I have {} lives left guys! Chill out, my power is {} but I wont hurt you".format(self.name, self.no_of_lives, self.power))


wizard1 = Wizard('Harry', 'unlimited', 1)

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User)) # returns true as well
print(isinstance(wizard1, object)) # returns true as well

print(issubclass(Wizard, User)) # returns true, function to check subclass


#note that python comes with a base object class and every object inherits from it. wizard1 inherits from Wizard class which inturn iherits from
# User which in turn inherits from the python base object class
#note that all the extra methods and attributes that we see being recommended for wizard1 come from the base object class

#note that every data type in python is an object so all objects (lists, tuples ... ) inherit methods and attributes from the python base object class

