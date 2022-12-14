from npc.languages import undercommon
from npc.generator.base import BaseNPC


class NPC(BaseNPC):

    ancestry = 'Drow'
    language = undercommon.DrowPerson()

    @property
    def full_name(self):
        return ' '.join([
            str(self.names[0]).capitalize(),
            str(self.names[1]).capitalize()
        ])
