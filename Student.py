
#Have your own datatype
#just defining a overview of the student datatype
class Student:

    def __init__(self, name, age, gpa, is_on_probation): #initialize
        self.name = name
        self.age = age
        self.gpa = gpa
        self.is_on_probation = is_on_probation #self refers to the actual object