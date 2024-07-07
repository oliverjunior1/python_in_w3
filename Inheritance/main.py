# class completeName:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def print_name(self):
#         print(self.fname + self.lname)

# x = completeName('Joaquim', ' Rodrigues')
# x.print_name()

###################################################

# class Numbers:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     def multiply(self):
#         return self.num1 * self.num2

# a = int(input('Put the first number: '))
# b = int(input('Put the second number: '))
# x = Numbers(a, b)
# print(x.multiply())

######################################################

# class completeName:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def print_name(self):
#         print(self.fname + self.lname)

# class Student(completeName):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#         self.graduationyear = 2019

# x = Student('Joaquim ', 'Rodrigues')
# x.print_name()
# print(x.graduationyear)

######################################################

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def completeName(self):
        print(self.fname + self.lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation = year

x = Student('Joaquim ', 'Rodrigues', 2019)
x.completeName()
print(x.graduation)



######################################################
######################################################