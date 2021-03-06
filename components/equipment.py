"""Component file for equipment

Equipments include:

-Weapons
-Armors
"""
from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Actor, Item


class Equipment(BaseComponent):
    """Base class for equipments"""
    parent: Actor

    def __init__(self,
                 left_hnd_wpn: Optional[Item] = None,
                 right_hnd_wpn: Optional[Item] = None,
                 body_armor: Optional[Item] = None,
                 head_armor: Optional[Item] = None,
                 gloves: Optional[Item] = None,
                 boots: Optional[Item] = None,
                 accessory: Optional[Item] = None,
                 ):
        self.left_hnd_wpn = left_hnd_wpn
        self.right_hnd_wpn = right_hnd_wpn
        self.head_armor = head_armor
        self.body_armor = body_armor
        self.gloves = gloves
        self.boots = boots
        self.accessory = accessory
# TODO: Modify useless equipment names and add others that are missing

    @property
    def defense_bonus(self) -> int:
        """Defense bonus given by the equipped item"""
        bonus = 0

        if self.left_hnd_wpn is not None and self.left_hnd_wpn.equippable is not None:
            bonus += self.left_hnd_wpn.equippable.defense_bonus

        if self.body_armor is not None and self.body_armor.equippable is not None:
            bonus += self.body_armor.equippable.defense_bonus

        return bonus

    @property
    def evasion_bonus(self) -> int:
        """Defense bonus given by the equipped item"""
        bonus = 0

        if self.left_hnd_wpn is not None and self.left_hnd_wpn.equippable is not None:
            bonus += self.left_hnd_wpn.equippable.evasion_bonus

        if self.body_armor is not None and self.body_armor.equippable is not None:
            bonus += self.body_armor.equippable.evasion_bonus

        return bonus

    @property
    def intelligence_bonus(self) -> int:
        """Defense bonus given by the equipped item"""
        bonus = 0

        if self.left_hnd_wpn is not None and self.left_hnd_wpn.equippable is not None:
            bonus += self.left_hnd_wpn.equippable.intelligence_bonus

        if self.body_armor is not None and self.body_armor.equippable is not None:
            bonus += self.body_armor.equippable.intelligence_bonus

        return bonus

    @property
    def damage_bonus(self) -> int:
        """Attack bonus given by the equipped item"""
        bonus = 0

        if self.left_hnd_wpn is not None and self.left_hnd_wpn.equippable is not None:
            bonus += self.left_hnd_wpn.equippable.power_bonus

        if self.body_armor is not None and self.body_armor.equippable is not None:
            bonus += self.body_armor.equippable.power_bonus

        return bonus

    def item_is_equipped(self, item: Item) -> bool:
        """Returns if the item is equipped or not"""
        return self.left_hnd_wpn == item or self.body_armor == item

    def unequip_message(self, item_name: str) -> None:
        """Message to show when you remove an item"""
        self.parent.gamemap.engine.message_log.add_message(
            f"You remove the {item_name}"
        )

    def equip_message(self, item_name: str) -> None:
        """Message to show when you equip an item"""
        self.parent.gamemap.engine.message_log.add_message(
            f"You equip the {item_name}"
        )

    def equip_to_slot(self, slot: str, item: Item, add_message: bool) -> None:
        """Handles the equipping of an item in the right slot"""
        current_item = getattr(self, slot)

        if current_item is not None:
            self.unequip_message(slot)

        setattr(self, slot, item)

        if add_message:
            self.equip_message(item.name)

    def unequip_from_slot(self, slot: str, add_message: bool) -> None:
        """Handles the unequipping of an item in the right slot"""
        current_item = getattr(self, slot)

        if add_message:
            self.unequip_message(current_item.name)

        setattr(self, slot, None)

    def toggle_equip(self, equippable_item: Item, add_message: bool = True) -> None:
        """Toggles the equipped/unequipped status of the chosen item"""
        if (
                equippable_item.equippable
                and equippable_item.equippable.equipment_type == EquipmentType.LEFT_HAND_WPN
                or equippable_item.equippable.equipment_type == EquipmentType.RIGHT_HAND_WPN
        ):
            slot = "left_hnd_wpn"
        else:
            slot = "body_armor"

        if getattr(self, slot) == equippable_item:
            self.unequip_from_slot(slot, add_message)
        else:
            self.equip_to_slot(slot, equippable_item, add_message)
