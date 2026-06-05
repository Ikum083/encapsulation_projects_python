# Assign a class named Fan
class Fan:
    ## construct for creating fan with the specified speed, radius, color and on/off
    def __init__(self, speed, radius, color, on_off):
    ## three constants named SLOW, MEDIUM AND FAST
        SLOW = 1
        MEDIUM = 2
        FAST = 3
## private int named speed for the speed of the fan
        self.__speed = speed
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
    
    def set_speed(self, radius):
        self.__radius = radius

    def set_speed(self, color):
        self.__color = color

    def set_speed(self, on_off):
        self.__on_status = on_off
    
fan = Fan(speed = 3, radius = 10, color = "yellow", on_off = "on")
### Test two fan objects
#### maximum speed, radius 10, color yellow and turn on
#### Medium speed, radius 5, rolor blue and turned off