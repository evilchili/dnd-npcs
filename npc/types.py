from npc import traits
import random
import dice
import textwrap
import logging

from typing import Union

from language.types import Name, Language


def a_or_an(s):
    return 'an' if s[0] in 'aeiouh' else 'a'


class StatBlock:

    def __init__(
        self,
        STR: int = 10,
        DEX: int = 10,
        CON: int = 10,
        INT: int = 10,
        WIS: int = 10,
        CHA: int = 10,
        HP: int = 10,
        AC: int = 10,
        speed: int = 30,
        passive_perception: int = 10,
        passive_investigation: int = 10,
    ):
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        self.HP = HP
        self.AC = AC
        self.speed = speed
        self.passive_perception = passive_perception
        self.passive_investigation = passive_investigation

    def randomize(self):
        stats = [15, 14, 13, 12, 10, 8]
        random.shuffle(stats)
        if random.random() < 0.3:
            i = random.choice(range(len(stats)))
            stats[i] += (random.choice([-1, 1]) * random.randint(1, 3))
        (self.STR, self.DEX, self.CON, self.INT, self.WIS, self.CHA) = stats
        self.HP = str(sum(dice.roll('2d8')) + 2) + ' (2d8+2)'

    def __str__(self):
        return textwrap.dedent(f"""
            AC  {self.AC}
            HP  {self.HP}
            STR {self.STR}
            DEX {self.DEX}
            CON {self.CON}
            INT {self.INT}
            WIS {self.WIS}
            CHA {self.CHA}

            Speed: {self.speed}

            Passive Perception: {self.passive_perception}
            Passive Investigation: {self.passive_perception}
        """)


class NPC:
    """
    Return a randomized NPC. Any supplied keyword parameters will override
    generated, randomized values.

    By default, NPC stats are all 10 (+0). If randomize is True, the NPC will
    be given random stats from the standard distribution, but overrides will
    still take precedence.
    """

    # Define this as a language module from language.supported_languages.values()
    language = None

    # appearance
    has_eyes = True
    has_hair = True
    has_face = True
    has_body = True
    has_nose = True
    has_lips = True
    has_teeth = True
    has_skin_tone = True
    has_skin_color = True
    has_facial_hair = True
    has_facial_structure = True
    has_eyebrows = True

    has_age = True
    has_voice = True

    has_tail = False
    has_horns = False
    has_fangs = False
    has_wings = False

    def __init__(
        self,
        name: Union[Name, None] = None,
        pronouns: Union[str, None] = None,
        whereabouts: str = "Unknown",
        stats: StatBlock = StatBlock(),
        noble: bool = False,
        randomize: bool = False,
        language: Union[Language, None] = None,
    ):

        # identity
        self._name = name
        self._is_noble = noble
        self._whereabouts = whereabouts
        self._stats = stats
        self._pronouns = pronouns

        # appearance
        self._eyes = None
        self._hair = None
        self._face = None
        self._body = None
        self._nose = None
        self._lips = None
        self._teeth = None
        self._skin_tone = None
        self._skin_color = None
        self._facial_hair = None
        self._facial_structure = None
        self._eyebrows = None
        self._age = None
        self._voice = None
        self._tail = None
        self._horns = None
        self._fangs = None
        self._wings = None

        # character
        self._flaw = None
        self._goal = None
        self._personality = None

        if language:
            self.language = language

        if randomize:
            self.stats.randomize()

    @property
    def ancestry(self) -> str:
        return self.__class__.__name__

    @property
    def names(self):
        if not self._names:
            self._names = next(self.name_generator.name(1))
        return self._names

    @property
    def full_name(self):
        """Legacy interface"""
        return self.name

    @property
    def is_noble(self) -> bool:
        return self._is_noble

    @property
    def name(self):
        if not self._name:
            generator = getattr(
                self.language,
                'NobleName' if self.is_noble else 'Name'
            )
            self._name = generator.name()[0]
            logging.debug(self._name)
        return self._name['fullname']

    @property
    def pronouns(self):
        if not self._pronouns:
            self._pronouns = random.choice([
                'he/him',
                'she/her',
                'they/they',
            ])
        return self._pronouns

    @property
    def title(self):
        return ' '.join(self.names.titles)

    @property
    def nickname(self):
        return ', '.join(self.names.nicknames)

    @property
    def whereabouts(self):
        return self._whereabouts

    @property
    def flaw(self):
        if self._flaw is None:
            self._flaw = random.choice(traits.flaws)
        return self._flaw

    @property
    def goal(self):
        if self._goal is None:
            self._goal = random.choice(traits.goals)
        return self._goal

    @property
    def personality(self):
        if self._personality is None:
            self._personality = ', '.join([
                random.choice(traits.personality),
                random.choice(traits.personality),
                random.choice(traits.personality),
            ])
        return self._personality

    @property
    def eyes(self):
        if self._eyes is None:
            self._eyes = ', '.join([random.choice(traits.eye_shape), random.choice(traits.eye_color)])
        return self._eyes

    @property
    def skin_color(self):
        if self._skin_color is None:
            self._skin_color = random.choice(traits.skin_color)
        return self._skin_color

    @property
    def skin_tone(self):
        if self._skin_tone is None:
            self._skin_tone = random.choice(traits.skin_tone)
        return self._skin_tone

    @property
    def hair(self):
        if self._hair is None:
            self._hair = ' '.join([random.choice(traits.hair_style), random.choice(traits.hair_color)])
        return self._hair

    @property
    def face(self):
        if not self._face:
            self._face = random.choice(traits.face)
        return self._face

    @property
    def facial_structure(self):
        if self._facial_structure is None:
            self._facial_structure = random.choice(traits.facial_structure)
        return self._facial_structure

    @property
    def lips(self):
        if self._lips is None:
            self._lips = random.choice(traits.lips)
        return self._lips

    @property
    def teeth(self):
        if self._teeth is None:
            self._teeth = random.choice(traits.teeth)
        return self._teeth

    @property
    def nose(self):
        if self._nose is None:
            self._nose = random.choice(traits.nose)
        return self._nose

    @property
    def eyebrows(self):
        if self._eyebrows is None:
            self._eyebrows = random.choice(traits.eyebrows)
        return self._eyebrows

    @property
    def facial_hair(self):
        if self._facial_hair is None:
            self._facial_hair = random.choice(traits.facial_hair)
        return self._facial_hair

    @property
    def body(self):
        if self._body is None:
            self._body = random.choice(traits.body)
        return self._body

    @property
    def tail(self):
        if self._tail is None:
            self._tail = random.choice(traits.tail)
        return self._tail

    @property
    def horns(self):
        if self._horns is None:
            self._horns = random.choice(traits.horns)
        return self._horns

    @property
    def wings(self):
        if self._wings is None:
            self._wings = random.choice(traits.wings)
        return self._wings

    @property
    def fangs(self):
        if self._fangs is None:
            self._fangs = random.choice(traits.fangs)
        return self._fangs

    @property
    def age(self):
        if not self._age:
            self._age = random.choice(traits.age)
        return self._age

    @property
    def voice(self):
        if not self._voice:
            self._voice = random.choice(traits.voice)
        return self._voice

    @property
    def stats(self):
        return self._stats

    @property
    def description(self):
        desc = (
            f"{self.name} ({self.pronouns}) is {a_or_an(self.age)} {self.age}, {self.body} "
            f"{self.ancestry.lower()} with {self.hair} hair, {self.eyes} eyes and {self.skin_color} skin."
        )
        trait = None
        while not trait:
            trait = random.choice([
                f'{self.eyebrows} eyebrows' if self.eyebrows else None,
                self.facial_hair if self.facial_hair else None,
                f'a {self.nose} nose' if self.nose else None,
                f'{self.lips} lips' if self.lips else None,
                f'{self.teeth} teeth' if self.teeth else None,
                self.facial_structure if self.facial_structure else None,
            ])
        desc = desc + ' ' + f"Their face is {self.face}, with {trait}."
        if self.has_tail:
            desc = desc + f" Their tail is {self.tail}."
        if self.has_horns:
            desc = desc + f" Their horns are {self.horns}."
        return desc

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
Horns:  {self.horns}
Fangs:  {self.fangs}
Wings:  {self.wings}
Voice: {self.voice}

Stats:
{textwrap.indent(str(self.stats), prefix='    ')}

Details:

Personality: {self.personality}
Flaw:        {self.flaw}
Goal:        {self.goal}

Whereabouts: {self.whereabouts}

"""

    def __repr__(self):
        return self.description
