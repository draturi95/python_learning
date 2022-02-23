
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


vehicle1 = Vehicle('Bolero', 160, 28)
vehicle2 = Bus('Roadwage bus', 110, 4.53, 64)

vehicle1.show()
vehicle2.show()

vehicle2.show_bus()



