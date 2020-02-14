# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle(object):#base class
    pass

class FlightVehicle(Vehicle):#base class
    pass

class Starship(FlightVehicle):#base class
    pass

class Airplane(FlightVehicle):#base class
    pass

class GroundVehicle(Vehicle):#base class
    pass

class Car(GroundVehicle):#base class
    pass
    
class Motorcycle(GroundVehicle):#base class
    pass