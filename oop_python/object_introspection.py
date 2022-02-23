# object introspection - the ability to determine the type of the program at runtime

# the function dir on an object gives me all the methods and attributes the object has access to


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def show(self):
        print('Name:', self.name)
        print('Max Speed of vehicle', self.max_speed)
        print('Mileage is', self.mileage)


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage)
        # could have also done Vehicle.__init__(self, name, max_speed, mileage) - NOTE that super doesnt take self as argument
        self.capacity = capacity

    def show_bus(self):
        print('Name:', self.name)
        print('Max Speed of vehicle', self.max_speed)
        print('Mileage is', self.mileage)
        print('Capacity is:', self.capacity)


print(dir(Bus))