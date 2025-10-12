"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.exceptions import CargoOverload
from homework_05.base import Vehicle


class Plane(Vehicle):

    def __init__(self, max_cargo, weight=0, started=False, fuel=0, fuel_consumption=0 ):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = None

    def load_cargo(self, input_cargo):
        cargo_summary = self.cargo + input_cargo
        if self.max_cargo < cargo_summary:
            raise CargoOverload

        self.cargo = cargo_summary

    def remove_all_cargo(self):
        previous_result = self.cargo
        self.cargo = 0
        return previous_result