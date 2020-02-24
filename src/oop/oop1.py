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

# Base class of Vehicle
class Vehicle:
  def __init__(self):
    pass

#  [Vehicle]->[FlightVehicle]
#  FlightVehicle should inhert from Vehicle
class FlightVehicle(Vehicle):
  def __init__(self):
    super().__init__()
    pass

#  [Vehicle]->[FlightVehicle]->[Starship]
#  Starship should inhert from FlightVehicle and Vehicle
class Starship(FlightVehicle):
  def __init__(self):
    super().__init__()
    pass

#  GroundVehicle should inhert from Vehicle
class GroundVehicle(Vehicle):
  def __init__(self):
    super().__init__()
    pass