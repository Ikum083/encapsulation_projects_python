# Assign a class named Fan
class Fan:
    ## construct for creating fan with the specified speed, radius, color and on/off
    def __init__(self, speed, radius, color, on_off):
    ## three constants named SLOW, MEDIUM AND FAST
        SLOW = 1
        MEDIUM = 2
        FAST = 3
        self.fan_speed = ""
## private int named speed for the speed of the fan
        self.__speed = speed
        if self.__speed == SLOW:
            self.fan_speed = "slow"
        elif self.__speed == MEDIUM:
            self.fan_speed = "medium"
        elif self.__speed == FAST:
            self.fan_speed = "fast"
        else:
            self.fan_speed = "unavailable fan speed"
## private bool to know if the fan is on or off
        self.__on_status = on_off
## private float to identify fan radius
        self.__radius = radius
## private string to identify fan color
        self.__color = color

    # accessor
    def get_speed(self):
        return self.__speed
    
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color
    
    def get_on_status(self):
        return self.__on_status
        
    # mutator
    def set_speed(self, speed):
        self.__speed = speed
    
    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_on_status(self, on_off):
        self.__on_status = on_off
    
if __name__ == "__main__":
    fan = Fan(1, 5, "blue", "on")

    # printing default fan object
    print(f"Default fan: ")
    print(f"Speed: {fan.get_speed()}")
    print(f"Radius: {fan.get_radius()}")
    print(f"Color: {fan.get_color()}")
    print(f"On/Off: {fan.get_on_status()}")

    ### Test two fan objects
    #### maximum speed, radius 10, color yellow and turn on
    fan.set_speed(3)
    fan.set_radius(10)
    fan.set_color("yellow")
    fan.set_on_status("on")

    print(f"\nModified fan #1: ")
    print(f"Speed: {fan.get_speed()}")
    print(f"Radius: {fan.get_radius()}")
    print(f"Color: {fan.get_color()}")
    print(f"On/Off: {fan.get_on_status()}")

    #### Medium speed, radius 5, color blue and turned off
    fan.set_speed(2)
    fan.set_radius(5)
    fan.set_color("blue")
    fan.set_on_status("off")

    print(f"\nModified fan #2: ")
    print(f"Speed: {fan.get_speed()}")
    print(f"Radius: {fan.get_radius()}")
    print(f"Color: {fan.get_color()}")
    print(f"On/Off: {fan.get_on_status()}")