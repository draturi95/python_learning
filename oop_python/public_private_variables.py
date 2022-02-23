#there are no private variables in python. So developers use a convention to let everyone using a code to know not to
#edit these particular attributes and methods. The convention is to simply use an _ in front of these attributes and methods


class CSStudent:
    class_stream = 'CSE'
    roll_count = 1

    def __init__(self, name):
        self._name = name
        self._roll_no = CSStudent.roll_count
        self.stream = CSStudent.class_stream
        CSStudent.roll_count = CSStudent.roll_count + 1

    def _introduction(self):
        print("Hey I'm {}, my roll no. is {} and they are in {} branch".format(self.name, self.roll_no, self.stream))

# note that here we have _introduction which is nothing different than regular methods. THe _ in the front is a convention
# for telling other developers to not reassign/mess with it in the program
#Eg. Don't do student1._introduction = 'BOOOO'