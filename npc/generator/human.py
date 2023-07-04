from npc.languages import common
from npc.generator.base import BaseNPC


class NPC(BaseNPC):

    ancestry = 'Human'
    language = common.CommonPerson()
