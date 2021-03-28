"""Modifiers are things that change an entity or item's behavior/stats"""
from typing import TYPE_CHECKING, Optional, List
from components.base_component import BaseComponent
from components.modifier_effects import ModifierFx
from rarity import Rarity

if TYPE_CHECKING:
    from entity import Item, Actor


class Modifier(BaseComponent):
    """Base class for modifiers"""
    def __init__(
        self,
        target_creature: Optional[Actor],
        target_item: Optional[Item],
        effects: List[ModifierFx],
        rarity: Rarity
    ):
        self.target_creature = target_creature
        self.target_item = target_item
        self.effects = effects
        self.rarity = rarity