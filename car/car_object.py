# Class Car with year model, make and speed
class Car:
## init method that takes year and make as arguments assigned to __year_model and __make, set default speed to 0
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0
## accelerate method to add 5 to speed
## brake method to subtract 5 to speed
## get_speed method to return speed
### Car object : Accelerate 5 times and brake 5 times