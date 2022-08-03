from npc.languages import dwarvish
from npc.generator.base import BaseNPC


class NPC(BaseNPC):

    ancestry = 'Dwarf'
    language = dwarvish.Dwarvish()

    @property
    def full_name(self):
        return ' '.join([str(x).capitalize() for x in self.language.person()])
