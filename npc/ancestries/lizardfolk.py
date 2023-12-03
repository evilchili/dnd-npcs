from functools import cached_property
import textwrap
import random

from language.languages import lizardfolk
from npc import types


class Lizardfolk(types.NPC):
    language = lizardfolk

    has_tail = True
    has_horns = True
    has_fangs = True

    @property
    def age(self):
        if not self._age:
            self._age = random.choice([
                'hatchling',
                'juvenile',
                'adult',
                'ancient',
            ])
        return self._age

    @property
    def tail(self):
        if not self._tail:
            if random.random() <= -0.6:
                self._tail = super(self)
            else:
                self._tail = 'no'
        return self._tail

    @cached_property
    def frills(self):
        if self.age in ('adult', 'ancient'):
            return random.choice([
                'orange',
                'red',
                'yellow',
                'green',
                'blue',
                'silvery',
            ])

    @property
    def skin_color(self):
        if not self._skin_color:
            self._skin_color = random.choice([
                'green',
                'blue',
                'grey',
                'brown',
                'tan',
                'sandy',
                'gold',
            ])
        return self._skin_color

    @property
    def description(self):
        trait = random.choice([
            f'{self.eyes} eyes',
            f'{self.tail} tail',
            f'{self.teeth} teeth',
            f'{self.frills} frills',
            self.facial_structure,
        ])
        return (
            f"{self.fullname} ({self.pronouns}) is {types.a_or_an(self.age)} {self.age}, {self.skin_color}-scaled "
            f"{self.ancestry.lower()} with {types.a_or_an(self.nose)} {self.nose} snout, {self.body} body and {trait}."
        )

    @property
    def character_sheet(self):
        desc = '\n'.join(textwrap.wrap(self.description, width=120))
        return f"""\

{desc}

Physical Traits:

Face:   {self.face}, {self.nose} snout, {self.teeth} teeth
Eyes:   {self.eyes}
Skin:   {self.skin_tone}
Scales: {self.skin_color}
Body:   {self.body}
Tail:   {self.tail}
Voice:  {self.voice}

Details:

Personality: {self.personality}
Flaw:        {self.flaw}
Goal:        {self.goal}

Whereabouts: {self.whereabouts}

"""


NPC = Lizardfolk
