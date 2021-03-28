"""Defines equipment types"""
from enum import auto, Enum


class EquipmentType(Enum):
    """Class defining equipment types"""
    LEFT_HAND_WPN = auto()
    RIGHT_HAND_WPN = auto()
    BODY_ARMOR = auto()
    HEAD_ARMOR = auto()
    GLOVES = auto()
    BOOTS = auto()
    ACCESSORY = auto()
