from language.languages import elvish
from npc import types


class Elf(types.NPC):
    language = elvish


NPC = Elf
