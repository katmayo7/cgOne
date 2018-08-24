"""
Blueprint class for cgOne
"""

from __future__ import absolute_import
from __future__ import print_function
from enum_classes import Type, Exterior, Interior, Colors, Fuel


class Blueprint:
    """
    A blueprint represents the initial design of car, storing
    information common to a make and model of car.
    """

    def __init__(self):
    	self.max_speed = 0
    	self.exhaust = 0
    	self.type = Type.hatchback
    	self.exterior = Exterior.aluminum
    	self.interior = Interior.fabric
    	self.make = 'Make'
    	self.model = 'Model'
    	self.colors = ['blue', 'red', 'green', 'white', 'black']
    	self.fuel = Fuel.petrol

    	self.performance = 0
    	self.emissions = 0
    	self.utility = 0

    def set_make(self, make_name):
        """
        assign a name for the make of the car
        """
    	self.make = make_name

    def set_model(self, model_name):
        """
        assign a name for the model of the car
        """
    	self.model = model_name

    def set_type(self, new_type):
        """
        assign the type of the car
        """
    	if not isinstance(new_type, Type):
            raise ValueError('Incorrect type')
    	self.type = new_type

    def set_exterior(self, new_ext):
        """
        assign the exterior material
        """
        if not isinstance(new_ext, Exterior):
            raise ValueError('Incorrect type')
    	self.exterior = new_ext

    def set_interior(self, new_int):
        """
        assign the interior materials
        """
        if not isinstance(new_int, Interior):
            raise ValueError('Incorrect type')
    	self.interior = new_int

    def set_colors(self, colors):
        """
        set available colors
        """
    	self.colors = colors

    def set_fuel(self, new_fuel):
        """
        set fuel type
        """
        if not isinstance(new_fuel, Fuel):
            raise ValueError('Incorrect type')
        self.fuel = new_fuel

    def print_details(self):
        """
        print out the car specs
        """
    	details = vars(self)
    	for d in details:
    		print(d + ': %s' % details[d])

#testing
if __name__ == '__main__':

    bp = Blueprint()
    #print(bp.fuel)
