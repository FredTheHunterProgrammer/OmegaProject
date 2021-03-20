"""
Creates basic entities for copying
"""
from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

orc = Actor(
    char="o",
    color=(32, 63, 32),
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

troll = Actor(
    char="T",
    color=(0, 63, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)
