# class completeName:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def print_name(self):
#         print(self.fname + self.lname)

# x = completeName('Joaquim', ' Rodrigues')
# x.print_name()

###################################################

class Numbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def multiply(self):
        return self.num1 * self.num2

a = int(input('Put the first number: '))
b = int(input('Put the second number: '))
x = Numbers(a, b)
print(x.multiply())