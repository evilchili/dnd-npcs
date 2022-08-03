from npc.languages import orcish
from npc.generator.base import BaseNPC


class NPC(BaseNPC):

    ancestry = 'Half-Orc'
    language = orcish.HalfOrcPerson()

    @property
    def full_name(self):
        return ' '.join([str(x).capitalize() for x in self.language.person()])
