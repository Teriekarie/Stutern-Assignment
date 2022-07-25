# program to create a class

class Car:
    
    def __init__(self, type, model, year, colour, capacity):
        self.type = type
        self.model = model
        self.year = year
        self.colour = colour
        self.capacity = capacity
        


# Adding methods
    def seating_capacity(self):
        return f"The seating capacity of a {self.type} is {self.capacity} passengers"
        
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_colour(self, colour):
        self.colour = colour
        
    def get_colour(self):
        return self.colour
    
    def speed_rate(self, speed):
        self.speed = speed
        return f"The speed rate of {self.model} is {self.speed} mph"
    
    def mileage_of_car(self, mileage):
        self.mileage = 0
        return f"The mileage of {self.model} is {self.mileage} because the car is still new"
 
mycar = Car('SUV', 'Kia sorento', 2009, 'Green', 4)

print(mycar.get_year())
print(mycar.get_colour())
print(mycar.seating_capacity())
print(mycar.speed_rate(45))
print(mycar.mileage_of_car(0))