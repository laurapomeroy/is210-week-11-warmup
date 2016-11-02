#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using subclassing to demonstrate has-a and is-a"""

import car


class CustomCar(car.Car):
    """A child class of car

    Args:
        color(str): The car's color.
        tires(list): a list of four instances.

    """
    def __init__(self, color='blue', tires=None):
        """Constructor for subclass CustomCar

        Args:
            tires(int): Number of tires.

        Returns:
        A list of tires.

        Examples:
            >>> mycar = CustomCar()
            >>> len(mycar.tires)
            4
            >>> isinstance(mycar.tires[0], CustomTire)
            True
        """
        car.Car.__init__(self, color)
        self.tires = tires
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(CustomTire())


class CustomTire(car.Tire):
    """Tires for a child class of car.

    Args:
        miles(numeric): How many miles the tire has.

    Attributes:
        __maximum_miles(int): A pseudo-private class attribute
    """
    __maximum_miles = 500
