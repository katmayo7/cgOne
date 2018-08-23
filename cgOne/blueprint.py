"""
Blueprint class for cgOne
"""

from __future__ import absolute_import
from __future__ import print_function


class Blueprint:
    """
    A blueprint represents the initial design of car, storing
    information common to a make and model of car.
    """

    def __init__(self):
    	self.max_speed = 0
    	self.exhaust = 0
    	self.type = 'Hatchback'
    	self.exterior = 'Aluminum'
    	self.interior = 'Fabric'
    	self.make = 'Make'
    	self.model = 'Model'
    	self.colors = ['blue', 'red', 'green', 'white', 'black']
    	self.fuel = 'Petrol'

    	self.performance = 0
    	self.emissions = 0
    	self.utility = 0

    #Assign a name for the make of the car
    def set_make(self, make_name):
    	self.make = make_name

    #Assign a name for the model of the car
    def set_model(self, model_name):
    	self.model = model_name

    #Assign the type of the car
    def set_type(self, val):
    	types = ['Hatchback', 'SUV', 'Sedan', 'Sport']
    	self.type = types[val]

    #Assign the exterior material
    def set_exterior(self, exterior):
    	ext = ['Aluminum', 'Steel', 'Lacquer']
    	self.exterior = ext[exterior]

    #Assign the interior materials
    def set_interior(self, interior):
    	interiors = ['Fabric', 'Leather']
    	self.interior = interiors[interior]

    #Set the available colors (colors is list)
    def set_colors(self, colors):
    	self.colors = colors

    #Set fuel type
    def set_fuel(self, f):
    	fuels = ['petrol', 'diesel', 'electricity']
    	self.fuel = fuels[f]

    #Print out the details of 
    def print_details(self):
    	details = vars(self)
    	for d in details:
    		print(d + ': %s' % details[d])

#testing
if __name__ == '__main__':
	bp = Blueprint()

	bp.print_details()