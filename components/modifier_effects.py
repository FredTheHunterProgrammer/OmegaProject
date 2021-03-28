"""Where all the modifier effects will be created"""
from typing import TYPE_CHECKING, Optional

from components.base_component import BaseComponent
from rarity import Rarity

if TYPE_CHECKING:
    from entity import Actor, Item


class ModifierFx(BaseComponent):
    """Base class for modifier effects"""
    def __init__(
            self,
            rarity: Rarity
    ):
        self.rarity = rarity




