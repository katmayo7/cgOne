"""
Player class for cgOne
"""

from __future__ import absolute_import
from __future__ import print_function


class Blueprint:
    """
    A player is the basis for human players and automated players.
    """

    def __init__(self):
        self.warehouses = []
        self.blueprints = []
