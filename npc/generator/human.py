from language.languages.common import common_name
from npc.generator.base import BaseNPC


class NPC(BaseNPC):

    ancestry = 'Human'
    name_generator = common_name
