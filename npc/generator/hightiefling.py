from npc.languages import infernal
from npc.generator import tiefling


class NPC(tiefling.NPC):
    language = infernal.HighTiefling()
