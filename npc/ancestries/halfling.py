from language.languages import halfling
from npc import types


class Halfling(types.NPC):
    language = halfling


NPC = Halfling
