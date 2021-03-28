"""Component file for modifiers
"""
from __future__ import annotations
from typing import TYPE_CHECKING
from components.base_component import BaseComponent
from equipment_types import EquipmentType
from rarity import Rarity

if TYPE_CHECKING:
    from entity import Actor, Item


class ModifierFx(BaseComponent):
    """Base class for modifier effects"""
    def __init__(self, inscribed_on: EquipmentType, rarity: Rarity):
        self.inscribed_on = inscribed_on,
        self.rarity = rarity