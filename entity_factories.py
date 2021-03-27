"""File where all unique creatures and items are stored"""
from components.ai import HostileEnemy
from components import consumable, equippable
from components.fighter import Fighter
from components.equipment import Equipment
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

"""Player"""

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_constitution=2, base_strength=5, base_agility=5, base_intelligence=4),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

"""Enemies"""

slime = Actor(
    char="J",
    color=(63, 127, 63),
    name="Slime",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_constitution=0, base_strength=3, base_agility=2, base_intelligence=1),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=355)
)

"""Consumables"""

# Potion
"""
Potions are items that are generally useful to the player when drinking them.
TODO : Make the potions throwable on an enemy (applying the potion's effects) 
"""

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Healing Potion",
    consumable=consumable.HealingConsumable(amount=4),
)

# Syringes
"""Syringes are items that the player can use on himself or a nearby enemy to apply a temporary effect."""

# Inscriptions
"""Like regular roguelike scrolls, but with a fancier word. Usually inscribed on a small plate of hard material."""

lightning_insc = Item(
    char="?",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

confusion_insc = Item(
    char="?",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_insc = Item(
    char="?",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

"""Equipment"""

dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger()
)

sword = Item(char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword())

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)
