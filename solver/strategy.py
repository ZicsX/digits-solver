# digits/solver/strategy.py

from enum import Enum

class Strategy(Enum):
    SHORTEST = 0
    LONGEST = 1

    def __str__(self):
        return self.name.title()

    @staticmethod
    def values():
        return list(Strategy)
