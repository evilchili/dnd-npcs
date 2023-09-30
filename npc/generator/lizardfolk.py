from npc.languages import lizardfolk
from npc.generator.base import BaseNPC, a_or_an

import textwrap
import random


class NPC(BaseNPC):

    ancestry = 'Lizardfolk'
    language = lizardfolk.Lizardfolk()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._tail = None
        self._horns = None
        self._fangs = None
        self._frills = None

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

    @property
    def frills(self):
        if not self._frills:
            if self.age in ('adult', 'ancient'):
                self._frills = random.choice([
                    'orange',
                    'red',
                    'yellow',
                    'green',
                    'blue',
                    'silvery',
                ])
        return self._frills

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
            f"{self.full_name} ({self.pronouns}) is {a_or_an(self.age)} {self.age}, {self.skin_color}-scaled "
            f"{self.ancestry.lower()} with {a_or_an(self.nose)} {self.nose} snout, {self.body} body and {trait}."
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
