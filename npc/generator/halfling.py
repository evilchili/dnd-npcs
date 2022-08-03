import random

from npc.languages import halfling
from npc.generator.base import BaseNPC


class NPC(BaseNPC):

    ancestry = 'Halfling'
    language = halfling.Halfling()
