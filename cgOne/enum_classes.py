from enum import Enum

"""
List of classes for Blueprint code
"""

class Type(Enum):
	hatchback = 1
	suv = 2
	sedan = 3
	sport = 4

class Exterior(Enum):
	aluminum = 1
	steel = 2
	lacquer = 3

class Interior(Enum):
	fabric = 1
	leather = 2

class Colors(Enum):
	pass

class Fuel(Enum):
	petrol = 1
	diesel = 2
	electric = 3