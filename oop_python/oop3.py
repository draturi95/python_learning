# @classmethod in python
#@staticmethod in python

class PlayerCharacter:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'Hey my name is {self.name} and Im {self.age} years old')

    @classmethod # class Methods have access to the class and it can modify a class state that would apply ot all instances of the class
    # it is bound to the class and not any object
    def adding_things(cls,  num1, num2):
        return num1 + num2

    @classmethod
    def instantiating_cls_with_classmethod(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod # Static methods do not have access to the class state. They are also bound to the class and not the instances of the class
    #They are generally utility type functions 
    def adding_things2(num1, num2):
        return num1 + num2

player = PlayerCharacter('East', 23)

print(PlayerCharacter.adding_things(45, 12))

print(PlayerCharacter(4, 12))

new_player = PlayerCharacter.instantiating_cls_with_classmethod(21, 211)

print(new_player.name, new_player.age)
