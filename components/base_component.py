from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity
    from game_map import GameMap


class BaseComponent:
    """Base component for every other component classes"""
    parent: Entity  # Owning entity instance

    @property
    def gamemap(self) -> GameMap:
        """Gamemap instance used for components"""
        return self.parent.gamemap

    @property
    def engine(self) -> Engine:
        """Engine instance used for components"""
        return self.gamemap.engine
