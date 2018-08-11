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
