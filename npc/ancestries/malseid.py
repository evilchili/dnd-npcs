import random

from npc import types
from language.languages import druidic

tail_traits = [
    'small',
    'clipped',
    'stubby',
    'stiff',
    'strong',
    'thick',
    'thin',
]


class Malseid(types.NPC):
    language = druidic
    has_tail = True

    @property
    def tail(self):
        if self._tail is None:
            self._tail = random.choice(tail_traits)
        return self._tail



NPC = Malseid
