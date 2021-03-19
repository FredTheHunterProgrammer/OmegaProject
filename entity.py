"""
Generic class to represent mostly everything in the game
"""

from typing import Tuple

class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
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

    def move(self, dx: int, dy: int) -> None:
        """
        Move the entity by a given amount
        :param dx: horizontal value to add
        :param dy: vertical value to add
        """
        self.x += dx
        self.y += dy
