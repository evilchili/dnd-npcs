from language.languages import dwarvish
from npc import types


class Dwarf(types.NPC):
    language = dwarvish


NPC = Dwarf
