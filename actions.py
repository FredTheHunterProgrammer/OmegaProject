"""
This is where the rogue's actions will be defined
"""

from __future__ import annotations
from typing import Optional, Tuple, TYPE_CHECKING

import color

if TYPE_CHECKING:
    from engine import Engine
    from entity import Actor, Entity


class Action:
    """
    Basic action class
    """

    def __init__(self, entity: Actor) -> None:
        super().__init__()
        self.entity = entity

    @property
    def engine(self) -> Engine:
        """Return the engine this action belongs to"""
        return self.entity.gamemap.engine

    def perform(self) -> None:
        """Perform this action with the objects needed to determine its scope.
        `engine` is the scope this action is being performed in.
        `entity` is the object performing the action.
        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()


class EscapeAction(Action):
    """
    Action to exit the game and close it
    """

    def perform(self) -> None:
        """
        Method to exit
        """
        raise SystemExit()


class WaitAction(Action):
    """Do nothing this turn"""
    def perform(self) -> None:
        """Wait"""
        pass


class ActionWithDirection(Action):
    """
    Choose the action to do in a given direction depending on the context
    """

    def __init__(self, entity: Actor, dx: int, dy: int):
        super().__init__(entity)

        self.dx = dx
        self.dy = dy

    @property
    def dest_xy(self) -> Tuple[int, int]:
        """Returns this actions destination"""
        return self.entity.x + self.dx, self.entity.y + self.dy

    @property
    def blocking_entity(self) -> Optional[Entity]:
        """Return the blocking entity at this actions destination"""
        return self.engine.game_map.get_blocking_entity_at_location(*self.dest_xy)

    @property
    def target_actor(self) -> Optional[Actor]:
        """Return the actor at this actions destination"""
        return self.engine.game_map.get_actor_at_location(*self.dest_xy)

    def perform(self) -> None:
        """
        Method that performs the action depending on the context
        """
        raise NotImplementedError()


class MeleeAction(ActionWithDirection):
    """
    A Melee attack
    """
    def perform(self) -> None:
        """
        Method to attack an enemy
        :return: None
        """
        target = self.target_actor
        if not target:
            return  # no entity to attack

        damage = self.entity.fighter.power - target.fighter.defense

        attack_desc = f"{self.entity.name.capitalize()} attacks {target.name}"
        if self.entity is self.engine.player:
            attack_color = color.player_atk
        else:
            attack_color = color.enemy_atk

        if damage > 0:
            self.engine.message_log.add_message(
                f"{attack_desc} for {damage} hit points.", attack_color
            )
            target.fighter.hp -= damage
        else:
            self.engine.message_log.add_message(
                f"{attack_desc} but does no damage", attack_color
            )


class MovementAction(ActionWithDirection):
    """
    Action that controls the character's movements
    """
    def perform(self) -> None:
        """
        Method for movement
        :return: None
        """
        dest_x, dest_y = self.dest_xy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):
            return  # Destination is out of bounds.
        if not self.engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return  # Destination is blocked by a tile
        if self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return  # Destination is blocked by an entity

        self.entity.move(self.dx, self.dy)


class BumpAction(ActionWithDirection):
    """
    Class deciding between attack or movement actions
    """
    def perform(self) -> None:
        """
        Method that chooses the good method between moving or attacking
        :return: None
        """
        if self.target_actor:
            return MeleeAction(self.entity, self.dx, self.dy).perform()
        else:
            return MovementAction(self.entity, self.dx, self.dy).perform()
