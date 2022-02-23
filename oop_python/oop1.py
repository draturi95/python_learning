class PlayerCharacter: # note that classes are named with camel case in python
    membership = True # this is a class object attribute. Unlike the class attributes, this isnt dynamic
    # note that class object attribute doesnt change accross the instances and is accessible by all instances of the class
    def __init__(self, name, age):
        if(self.membership): # also can be accessed by PlayerCharacter.membership
            self.name = name
            self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('East', 23)
player2 = PlayerCharacter('Mritunjay', 5)

print(player1)
player1.membership = False
print(player1.membership)
print(player2.membership )