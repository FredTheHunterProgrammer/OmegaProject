"""File defining equippable items"""
from __future__ import annotations
from typing import TYPE_CHECKING
from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item


class Equippable(BaseComponent):
    """Base class of equippable items"""
    parent: Item

    def __init__(
            self,
            equipment_type: EquipmentType,
            power_bonus: int = 0,
            defense_bonus: int = 0,
            evasion_bonus: int = 0,
    ):
        self.equipment_type = equipment_type
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.evasion_bonus = evasion_bonus


class Dagger(Equippable):
    """Characteristics of an instance of a DAGGER weapon"""

    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=2)


class Sword(Equippable):
    """Characteristics of an instance of a SWORD weapon"""

    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=4)


class LeatherArmor(Equippable):
    """Characteristics of an instance of a LEATHER ARMOR"""

    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, defense_bonus=1)


class ChainMail(Equippable):
    """Characteristics of an instance of a CHAIN MAIL ARMOR"""

    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, defense_bonus=3)
