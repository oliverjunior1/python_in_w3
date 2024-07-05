# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def my_func(abc):
#         print(f'Hello my name is {abc.name} and my age is {abc.age}.' )
# p1 = Person('John', 36)
# p1.my_func()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print('Hello my name is ' + self.name)
# p1 = Person('John', 36)
# p1.age = 40
# print(p1.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('John', 36)
print(p1.name)
print(p1.age)
