"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    """Ошибка 1"""

    def __init__(self, message="Что-то там... 1"):
        self.message = message
        super().__init__(self.message)

class NotEnoughFuel(Exception):
    """Ошибка 1"""

    def __init__(self, message="Что-то там... 2"):
        self.message = message
        super().__init__(self.message)

class CargoOverload(Exception):
    """Ошибка 3"""

    def __init__(self, message="Что-то там... 3"):
        self.message = message
        super().__init__(self.message)
