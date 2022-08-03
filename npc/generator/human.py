from npc.languages import common
from npc.generator.base import BaseNPC


class NPC(BaseNPC):

    ancestry = 'Human'
    language = common.CommonPerson()

    @property
    def full_name(self):
        return ' '.join([str(x).capitalize() for x in self.language.person()])
