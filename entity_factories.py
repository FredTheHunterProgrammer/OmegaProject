"""
Creates basic entities for copying
"""
from entity import Entity

player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movement=True)
orc = Entity(char="o", color=(32, 63, 32), name="Orc", blocks_movement=True)
troll = Entity(char="T", color=(0, 63, 0), name="Troll", blocks_movement=True)
