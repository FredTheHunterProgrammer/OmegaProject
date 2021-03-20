from __future__ import annotations

from typing import Iterable, TYPE_CHECKING

import numpy as np
from tcod.console import Console

import tile_types

if TYPE_CHECKING:
    from entity import Entity

class GameMap:
    def __init__(self, width: int, height: int, entities: Iterable[Entity] = ()):
        self.width, self.height = width, height
        self.entities = set(entities)
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F") # Tiles the player can currently see
        self.explored = np.full((width, height), fill_value=False, order="F") # Tiles the player has seen before

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0<= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.
        If a tile is in the "visible" array, then draw it with the "light" colors.
        if it isn't but it's in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHROUD".
        :param console: The console used for showing the game
        :return: Nothing
        """
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD
        )


        for entity in self.entities:
            # Only print entities that are in FOV
            if self.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, string=entity.char, fg=entity.color)