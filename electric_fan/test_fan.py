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
## Accessor and Mutator method for all four data fields
### Test two fan objects
#### maximum speed, radius 10, color yellow and turn on
#### Medium speed, radius 5, rolor blue and turned off