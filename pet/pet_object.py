# create pet class with __name, __animal_type and __age
class Pet:
## init method that contains the name, animal type and age variables
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
## set name, animal type and age
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

## get name, animal type and age
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_animal_type(self):
        return self.__animal_type
    
### prompt user to input their pet's attributes
if __name__ == "__main__":
    pet = Pet("Buddy", "Dog", 10)

    name = input("Enter your pet's name: ")
    animal_type = input("What animal is your pet?: ")
    age = int(input("Enter your pet's age: "))

    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)

    print("")

    print(f"Pet name: {pet.get_name()}")
    print(f"Pet animal type: {pet.get_animal_type()}")
    print(f"Pet age: {pet.get_age()}")