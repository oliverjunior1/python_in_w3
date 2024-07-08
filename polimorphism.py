class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        
    def sound(self):
        print('Bruuum')

class Helicopter:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        
    def sound(self):
        print('Veuveuveuveuveu')

class Ambulance:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        
    def sound(self):
        print('Uuiuuuiuuui')

car = Car('Gol', 1998)
helicopter = Helicopter('Strenght', 2020)
ambulance = Ambulance('Volvo', 2022)

for x in (car, helicopter, ambulance):
    x.sound()

