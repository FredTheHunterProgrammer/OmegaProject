"""Handles the character's level, and levelling up"""
from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor


class Level(BaseComponent):
    """Base class for a character's level"""
    parent: Actor

    def __init__(
            self,
            current_level: int = 1,
            current_xp: int = 0,
            level_up_base: int = 0,
            level_up_factor: int = 150,
            xp_given: int = 0,
    ):
        self.current_level = current_level
        self.current_xp = current_xp
        self.level_up_base = level_up_base
        self.level_up_factor = level_up_factor
        self.xp_given = xp_given

    @property
    def experience_to_next_level(self) -> int:
        """Defines the exp required to level up"""
        return self.level_up_base + self.current_level * self.level_up_factor

    @property
    def requires_level_up(self) -> bool:
        """Check if the amount of xp gained brings you to the next level or not"""
        return self.current_xp > self.experience_to_next_level

    def add_xp(self, xp: int) -> None:
        """Adds xp to your xp total"""
        if xp == 0 or self.level_up_base == 0:
            return

        self.current_xp += xp

        self.engine.message_log.add_message(f"You gain {xp} experience points")

        if self.requires_level_up:
            self.engine.message_log.add_message(
                f"You advance to level {self.current_level + 1}!"
            )

    def increase_level(self) -> None:
        """Level up and bring your level to +1"""
        self.current_xp -= self.experience_to_next_level
        self.current_level += 1

    def increase_max_hp(self, amount: int = 20) -> None:
        """Increases your max health"""
        self.parent.fighter.max_hp += amount
        self.parent.fighter.hp += amount

        self.engine.message_log.add_message("Your health improves!")

        self.increase_level()

    def increase_power(self, amount: int = 1) -> None:
        """Increases your base damage"""
        self.parent.fighter.base_power += amount
        self.engine.message_log.add_message("You feel stronger!")

    def increase_defense(self, amount: int = 1) -> None:
        """Increases your base defense"""
        self.parent.fighter.base_defense += amount
        self.engine.message_log.add_message("Your movements are getting swifter!")

        self.increase_level()
