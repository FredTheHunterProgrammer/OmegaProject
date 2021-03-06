"""File defining a fighting entity's characteristics/stats"""
from __future__ import annotations

from typing import TYPE_CHECKING

import color
from components.base_component import BaseComponent
from render_order import RenderOrder

if TYPE_CHECKING:
    from entity import Actor


class Fighter(BaseComponent):
    """Base fighter class"""
    parent: Actor

    def __init__(self, hp: int, base_constitution: int, base_strength: int, base_agility: int, base_intelligence: int):
        self.max_hp = hp
        self._hp = hp
        self.base_constitution = base_constitution
        self.base_strength = base_strength
        self.base_agility = base_agility
        self.base_intelligence = base_intelligence

    @property
    def hp(self) -> int:
        """Character's health"""
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.parent.ai:
            self.die()

    @property
    def constitution(self) -> int:
        """Character's defense"""
        return self.base_constitution + self.defense_bonus

    @property
    def strength(self) -> int:
        """Character's power"""
        return self.base_strength + self.damage_bonus

    @property
    def agility(self) -> int:
        """Character's power"""
        return self.base_agility + self.agility_bonus

    @property
    def intelligence(self) -> int:
        """Character's power"""
        return self.base_intelligence + self.intelligence_bonus

    @property
    def defense_bonus(self) -> int:
        """Character's bonus defense given by equipment"""
        if self.parent.equipment:
            return self.parent.equipment.defense_bonus
        else:
            return 0

    @property
    def damage_bonus(self) -> int:
        """Character's bonus power given by equipment"""
        if self.parent.equipment:
            return self.parent.equipment.damage_bonus
        else:
            return 0

    @property
    def agility_bonus(self) -> int:
        """Character's bonus power given by equipment"""
        if self.parent.equipment:
            return self.parent.equipment.evasion_bonus
        else:
            return 0

    @property
    def intelligence_bonus(self) -> int:
        """Character's bonus power given by equipment"""
        if self.parent.equipment:
            return self.parent.equipment.intelligence_bonus
        else:
            return 0

    def die(self) -> None:
        """Handles a character's death.
        If player, end game;
        if enemy, continue."""
        if self.engine.player is self.parent:
            death_message = "You died!"
            death_message_color = color.player_die
        else:
            death_message = f"{self.parent.name} is dead!"
            death_message_color = color.enemy_die

        self.parent.char = "%"
        self.parent.color = (191, 0, 0)
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.name = f"remains of {self.parent.name}"
        self.parent.render_order = RenderOrder.CORPSE

        self.engine.message_log.add_message(death_message, death_message_color)

        self.engine.player.level.add_xp(self.parent.level.xp_given)

    def heal(self, amount: int) -> int:
        """Handles healing of a character"""
        if self.hp == self.max_hp:
            return 0

        new_hp_value = self.hp + amount

        if new_hp_value > self.max_hp:
            new_hp_value = self.max_hp

        amount_recovered = new_hp_value - self.hp

        self.hp = new_hp_value

        return amount_recovered

    def take_damage(self, amount: int) -> None:
        """Handles a character taking damage"""
        self.hp -= amount
