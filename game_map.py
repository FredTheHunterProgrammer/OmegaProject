"""
Controls the game map
"""
from __future__ import annotations

from typing import Iterable, Iterator, Optional, TYPE_CHECKING

import numpy as np
from tcod.console import Console

from entity import Actor
import tile_types

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class GameMap:
    """
    Class with all of the game map's functions
    """

    def __init__(self, engine: Engine, width: int, height: int, entities: Iterable[Entity] = ()):
        self.engine = engine
        self.width, self.height = width, height
        self.entities = set(entities)
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full(
            (width, height), fill_value=False, order="F"
        )  # Tiles the player can currently see
        self.explored = np.full(
            (width, height), fill_value=False, order="F"
        )  # Tiles the player has seen before

    @property
    def actors(self) -> Iterator[Actor]:
        """Iterate over this maps living actors"""
        yield from (
            entity
            for entity in self.entities
            if isinstance(entity, Actor) and entity.is_alive
        )

    def get_blocking_entity_at_location(self, location_x: int, location_y: int) -> Optional[Entity]:
        """
        Checks if an entity is blocking your way
        :param location_x: Horizontal position of the enitity
        :param location_y: Vertical position of the entity
        :return: The blocking entity if applicable
        """
        for entity in self.entities:
            if (
                    entity.blocks_movement
                    and entity.x == location_x
                    and entity.y == location_y
            ):
                return entity
        return None

    def get_actor_at_location(self, x: int, y: int) -> Optional[Actor]:
        """Self explanatory"""
        for actor in self.actors:
            if actor.x == x and actor.y == y:
                return actor

    def in_bounds(self, x: int, y: int) -> bool:
        """
        Checks where the inside of a room would be
        :param x: horizontal center of the room
        :param y: Vertical center of the room
        :return: True if the inside of a room is valid
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.
        If a tile is in the "visible" array, then draw it with the "light" colors.
        if it isn't but it's in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHROUD".
        :param console: The console used for showing the game
        :return: Nothing
        """
        console.tiles_rgb[0: self.width, 0: self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD,
        )

        entities_sorted_for_rendering = sorted(
            self.entities, key=lambda x: x.render_order.value
        )

        for entity in entities_sorted_for_rendering:
            # Only print entities that are in FOV
            if self.visible[entity.x, entity.y]:
                console.print(
                    x=entity.x, y=entity.y, string=entity.char, fg=entity.color)
