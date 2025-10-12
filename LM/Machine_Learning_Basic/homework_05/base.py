"""
Доработайте класс `Vehicle`
"""

from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False and self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError

    def move(self, distance_fuel):
        if self.fuel >= distance_fuel:
            self.fuel = self.fuel - distance_fuel
        else:
            raise NotEnoughFuel
