"""
This is where the rogue's actions will be defined
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class Action:
    """
    Basic action class
    """

    def perform(self, engine: Engine, entity: Entity) -> None:
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

    def perform(self, engine: Engine, entity: Entity) -> None:
        """
        Method to exit
        :param engine: Not used yet
        :param entity: Not used yet
        :return: None
        """
        raise SystemExit()


class ActionWithDirection(Action):
    """
    Choose the action to do in a given direction depending on the context
    """

    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:
        """
        Method that performs the action depending on the context
        :param engine:
        :param entity:
        :return:
        """
        raise NotImplementedError()


class MeleeAction(ActionWithDirection):
    """
    A Melee attack
    """

    def perform(self, engine: Engine, entity: Entity) -> None:
        """
        Method to attack an enemy
        :param engine: Engine used
        :param entity: Entity doing the action
        :return: None
        """
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
        if not target:
            return  # no entity to attack

        print(f"You kick the {target.name}, much to its annoyance!")


class MovementAction(ActionWithDirection):
    """
    Action that controls the character's movements
    """

    def perform(self, engine: Engine, entity: Entity) -> None:
        """
        Method for movement
        :param engine: the engine used
        :param entity: the entity moving
        :return: None
        """
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return  # Destination is out of bounds.
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return  # Destination is blocked by a tile
        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return  # Destination is blocked by an entity

        entity.move(self.dx, self.dy)


class BumpAction(ActionWithDirection):
    """
    Class deciding between attack or movement actions
    """
    def perform(self, engine: Engine, entity: Entity) -> None:
        """
        Method that chooses the good method between moving or attacking
        :param engine: Engine used
        :param entity: The creature doing the action
        :return: None
        """
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return MeleeAction(self.dx, self.dy).perform(engine, entity)
        else:
            return MovementAction(self.dx, self.dy).perform(engine, entity)
