"""
This is where the rogue's actions will be defined
"""

from __future__ import annotations
from typing import Optional, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class Action:
    """
    Basic action class
    """
    def __init__(self, entity: Entity) -> None:
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
    def perform(self) -> None:
        pass

class ActionWithDirection(Action):
    """
    Choose the action to do in a given direction depending on the context
    """

    def __init__(self, entity: Entity, dx: int, dy: int):
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
        :param engine: Engine used
        :param entity: Entity doing the action
        :return: None
        """
        target = self.blocking_entity
        if not target:
            return  # no entity to attack

        print(f"You kick the {target.name}, much to its annoyance!")


class MovementAction(ActionWithDirection):
    """
    Action that controls the character's movements
    """

    def perform(self) -> None:
        """
        Method for movement
        :param engine: the engine used
        :param entity: the entity moving
        :return: None
        """
        dest_x , dest_y = self.dest_xy

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
        :param engine: Engine used
        :param entity: The creature doing the action
        :return: None
        """
        if self.blocking_entity:
            return MeleeAction(self.entity, self.dx, self.dy).perform()
        else:
            return MovementAction(self.entity, self.dx, self.dy).perform()
