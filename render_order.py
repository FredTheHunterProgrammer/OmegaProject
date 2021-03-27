"""File for rendering order of items on the screen"""
from enum import auto, Enum


class RenderOrder(Enum):
    """Order is: Actor > Item > Corpse"""
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()
