from language.languages import common
from npc import types


class Human(types.NPC):
    language = common


NPC = Human
