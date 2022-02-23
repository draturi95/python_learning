# multiple inheritance in python

# note that here the class HybridBorg inherits from two classes Wizard and Archer. Note that in order to user methods of each of these classes, we must initiate the attributes of these classes that are being used in these methods
# For eg: in order to call hybrid_borg.attack(), we must initiate the power and name for the wizard class instant that is in hybrid_brog
# Note that in HybridBorg, we initiate both Wizard and Archer class so we can access the methods of these classes for hybrid_borg

class User(object):
    def __init__(self, email):
        self.email = email
        print('init complete ')

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with {self.power} power, this is your boy {self.name}')


class Archer(User):
    def __init__(self, email, name, arrows):
        super().__init__(email)
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'arrows remaining: {self.arrows}')


class HybridBorg(Wizard, Archer):
    def __init__(self, email, name, power, arrows):
        Wizard.__init__(self, name, power)  # important line, dont miss it
        Archer.__init__(self,email, name, arrows)  # important line, dont miss it. In order to call check_arrows(), we must first initiate arrows property for Archer instance


hybrid_borg = HybridBorg('ron@hmail.com','Ron', 'unlimited', 999)

hybrid_borg.attack()
hybrid_borg.check_arrows()


