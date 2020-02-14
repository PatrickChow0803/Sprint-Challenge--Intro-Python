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

    #This is the base class
class Vehicle():
    pass

    #This class inherits from Vehicle
class FlightVehicle(Vehicle):
    pass

    #This class inherits from FlightVehicle
class Starship(FlightVehicle):
    pass

    #This class inherits from FlightVehicle
class Airplane(FlightVehicle):
    pass

    #This class inherits from Vehicle
class GroundVehicle(Vehicle):
    pass

    #This class inherits from GroundVehicle
class Car(GroundVehicle):
    pass

    # This class inherits from GroundVehicle
class Motorcycle(GroundVehicle):
    pass
