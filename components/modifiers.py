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
    def __init__(self, rarity: Rarity):
        self.rarity = rarity


class EnemyModifierFx(ModifierFx):
    """Class for basic enemy modifiers. TODO: Start with secondary mods"""
    def __init__(self, rarity: Rarity, enemy: Actor):
        super().__init__(rarity)
        self.enemy = enemy


class ItemsModifierFx(ModifierFx):
    """Class for basic item modifiers"""
    def __init__(self, rarity: Rarity, item: Item):
        super().__init__(rarity)
        self.item = item
