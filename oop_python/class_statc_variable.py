# class and static variable - in C++ or java, they have static keyword to initialise them
# note that any variable inside a method in a class in python is non static variable nad any variable which is in the class
# roll_count is a static  class variable
#NOTE: always change the class variable by saying CLassName.class_variable = ... and not through a particular object of the class
# because changing by the class variable will change it across all instances but if we change it by an object,
#a new instance variable is created for that particular object, which shadows the class variables

# class and static variable - in C++ or java, they have static keyword to initialise them
# note that any variable inside a method in a class in python is non static variable nad any variable which is in the class
# roll_count is a static  class variable
# NOTE: always change the class


class CSStudent:
    class_stream = 'CSE'
    roll_count = 1

    def __init__(self, name):
        self.name = name
        self.roll_no = CSStudent.roll_count
        # note that cssstudent.roll_count can also be accesed as self.roll_count. That's why dont name roll_count also as roll_no cause we'd have the
        #same name self.roll_no for both the class variable and the object's roll no causing class variable to shadow
        self.stream = CSStudent.class_stream

        CSStudent.roll_count = CSStudent.roll_count + 1
        # aways change class variable by accessing it via class name. If you try by object name, it will only change for that particuular
        # object and not for all objects

    def introduction(self):
        print("Hey I'm {}, my roll no. is {} and they are in {} branch".format(self.name, self.roll_no, self.stream))


student1 = CSStudent('Dhawal')
student2 = CSStudent('Herika')

student1.introduction()
student2.introduction()

CSStudent.class_stream = 'Mech'
#note that this changes the class_stream to mech in the class but student1 & student2 still PRINT cs as it was stored in their
# object property stream but now when I print student1.class_stream, it'd would have changed to mech



student3 = CSStudent('Tamonud')


student1.introduction()
student2.introduction()
student3.introduction()


#note that if we now do student1.introduction  = 'booo', now if we access, student1.introduction() we get error because for student1 now
#introductionn ahs been modified


