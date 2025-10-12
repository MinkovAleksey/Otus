"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    """Ошибка возникает если ниизкий уровень запаса топлива"""

    def __init__(self, message="Низкий уровень топлива"):
        self.message = message
        super().__init__(self.message)

class NotEnoughFuel(Exception):
    """Ошибка возникает при недостаточности топтила"""

    def __init__(self, message="Недостаточно топлива"):
        self.message = message
        super().__init__(self.message)

class CargoOverload(Exception):
    """Ошибка возникает при перегрузе"""

    def __init__(self, message="Перегруз"):
        self.message = message
        super().__init__(self.message)
