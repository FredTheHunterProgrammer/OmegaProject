"""Handle the loading and initialization of game sessions"""
from __future__ import annotations

import copy
from typing import Optional

import tcod
import color
from engine import Engine
import entity_factories
import input_handlers
from procgen import generate_dungeon