"""Values for item and enemy rarity"""
from enum import auto, Enum


class Rarity(Enum):
    """Class defining rarities"""
    COMMON = auto()
    RARE = auto()
    SPECIAL = auto()
