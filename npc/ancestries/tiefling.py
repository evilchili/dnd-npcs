import random

from language.languages import infernal
from npc import types


class Tiefling(types.NPC):
    language = infernal

    has_tail = True
    has_horns = True
    has_fangs = True

    @property
    def skin_color(self):
        if not self._skin_color:
            self._skin_color = random.choice([
                'reddish',
                'white',
                'green',
                'black',
                'blue',
                'brassy',
                'bronze',
                'coppery',
                'silvery',
                'gold',
            ])
        return self._skin_color


NPC = Tiefling
