"""
Generic class to represent mostly everything in the game
"""

from __future__ import annotations

from numpy import copy
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar("T", bound="Entity")

class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self,
                 x: int = 0,
                 y: int = 0,
                 char: str = "?",
                 color: Tuple[int, int, int] = (255,255,255),
                 name: str = "<Unnamed>",
                 blocks_movement: bool = False,
    ):
        """
        Initializer for an entity
        :param x: horizontal position
        :param y: vertical position
        :param char: character representing the entity
        :param color: color of the entity
        """
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement


    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        """Spawn a copy of this instance at the given location"""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gamemap.entities.add(clone)
        return clone


    def move(self, dx: int, dy: int) -> None:
        """
        Move the entity by a given amount
        :param dx: horizontal value to add
        :param dy: vertical value to add
        """
        self.x += dx
        self.y += dy
