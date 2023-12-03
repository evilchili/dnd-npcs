from functools import cached_property
from npc import types
import textwrap
import random

from language.languages import draconic


class Dragon(types.NPC):

    language = draconic
    is_noble = True

    has_tail = True
    has_horns = True
    has_fangs = True
    has_wings = True


    @cached_property
    def age(self) -> str:
        return random.choice(['wyrmling', 'young', 'adult', 'ancient'])

    @cached_property
    def pronouns(self) -> str:
        return 'they/they'

    @property
    def skin_color(self):
        if not self._skin_color:
            self._skin_color = random.choice([
                'red',
                'white',
                'green',
                'black',
                'blue',
                'brass',
                'bronze',
                'copper',
                'silver',
                'gold',
            ])
        return self._skin_color

    @property
    def description(self):
        trait = random.choice([
            f'{self.eyes} eyes',
            f'{self.tail} tail',
            f'{self.eyebrows} eyebrows',
            f'{self.teeth} fangs',
            self.facial_structure,
        ])
        return (
            f"{self.name} ({self.pronouns}) is {types.a_or_an(self.age)} {self.age} {self.skin_color} "
            f"{self.ancestry.lower()} with {types.a_or_an(self.nose)} {self.nose} snout, {self.body} body and {trait}."
        )

    @property
    def character_sheet(self):
        desc = '\n'.join(textwrap.wrap(self.description, width=120))
        return f"""\

{desc}

Physical Traits:

Face:  {self.face}, {self.eyebrows} eyebrows, {self.nose} nose, {self.lips} lips,
       {self.teeth} teeth, {self.facial_hair}
Eyes:  {self.eyes}
Skin:  {self.skin_tone}, {self.skin_color}
Hair:  {self.hair}
Body:  {self.body}
Tail:  {self.tail}
Voice: {self.voice}

Details:

Personality: {self.personality}
Flaw:        {self.flaw}
Goal:        {self.goal}

Whereabouts: {self.whereabouts}

"""


NPC = Dragon
