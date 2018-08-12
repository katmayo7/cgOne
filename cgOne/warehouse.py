"""
Warehouse class for cgOne
"""

from __future__ import absolute_import
from __future__ import print_function


class Warehouse:
    """
    A warehouse is used for storing raw goods and has two
    primary fields: total_capacity and used_capacity. Under
    this model, warehouses do not care about the size of the
    object being stored, as raw goods are assumed to be of
    roughly uniform size.
    """

    def __init__(self):
        self.total_capacity = 0
        self.used_capacity = 0
