from npc.generator.base import generate_npc, npc_type
from npc import languages

import random
import typer
from enum import Enum

from rich import print


class Ancestry(str, Enum):
    dragon = 'dragon'
    drow = 'drow'
    dwarf = 'dwarf'
    elf = 'elf'
    halfling = 'halfling'
    halforc = 'halforc'
    highelf = 'highelf'
    highttiefling = 'hightiefling'
    human = 'human'
    tiefling = 'tiefling'


class Language(str, Enum):
    abyssal = 'abyssal'
    celestial = 'celestial'
    common = 'commmon'
    draconic = 'draconic'
    dwarvish = 'dwarvish'
    elven = 'elven'
    gnomish = 'gnomish'
    halfling = 'halfing'
    infernal = 'infernal'
    orcish = 'orcish'
    undercommon = 'undercommon'


app = typer.Typer()


@app.command()
def npc(
    ancestry: Ancestry = typer.Option(
        None,
        help='Derive NPC characteristics from a specific ancestry. Randomized if not specified.',
    ),
    name: str = typer.Option(
        None,
        help='Specify the NPC name. Randomized names are derived from ancestry',
    ),
    pronouns: str = typer.Option(
        None,
        help='Specify the NPC pronouns.',
    ),
    title: str = typer.Option(
        None,
        help='Specify the NPC title.',
    ),
    nickname: str = typer.Option(
        None,
        help='Specify the NPC nickname.',
    ),
    whereabouts: str = typer.Option(
        None,
        help='Specify the NPC whereabouts.',
    ),
    STR: str = typer.Option(
        None,
        help='Specify the NPC strength score.',
    ),
    DEX: str = typer.Option(
        None,
        help='Specify the NPC dexterity score.',
    ),
    CON: str = typer.Option(
        None,
        help='Specify the NPC constitution score.',
    ),
    INT: str = typer.Option(
        None,
        help='Specify the NPC intelligence score.',
    ),
    WIS: str = typer.Option(
        None,
        help='Specify the NPC wisdom score.',
    ),
    CHA: str = typer.Option(
        None,
        help='Specify the NPC charisma score.',
    ),
    randomize: bool = typer.Option(
        False,
        help='If True, randomize default stat scores. If False, all stats are 10.'
    ),
) -> None:
    """
    Generate a basic NPC.
    """
    print(generate_npc(
        ancestry=ancestry,
        names=name.split() if name else [],
        pronouns=pronouns,
        title=title,
        nickname=nickname,
        whereabouts=whereabouts,
        STR=STR,
        DEX=DEX,
        CON=CON,
        INT=INT,
        WIS=WIS,
        CHA=CHA,
        randomize=randomize
    ).character_sheet)


@app.command()
def names(ancestry: Ancestry = typer.Option(
        None,
        help='Derive NPC characteristics from a specific ancestry. Randomized if not specified.',
    ),
    count: int = typer.Option(
        1,
        help='How many names to generate.'
    ),
) -> None:
    for _ in range(int(count)):
        print(npc_type(ancestry)().full_name)


@app.command()
def text(
    language: Language = typer.Option(
        'common',
        help='The language for which to generate text.',
    ),
    count: int = typer.Argument(
        50,
        help='How many words to generate.'
    ),
) -> None:
    mod = getattr(languages, language, None)
    if not mod:
        print(f'Unsupported Language: {language}.')
        return
    lang_class = getattr(mod, language.capitalize(), None)
    if not lang_class:
        print(f'Unsupported Language: {language} in {mod}.')
        return
    lang = lang_class()

    phrases = []
    phrase = []
    for word in [lang.word() for _ in range(int(count))]:
        phrase.append(str(word))
        if len(phrase) >= random.randint(1, 12):
            phrases.append(' '.join(phrase))
            phrase = []
    if phrase:
        phrases.append(' '.join(phrase))

    paragraph = phrases[0].capitalize()
    for phrase in phrases[1:]:
        if random.choice([0, 0, 1]):
            paragraph = paragraph + random.choice('?!.') + ' ' + phrase.capitalize()
        else:
            paragraph = paragraph + ', ' + phrase
    print(f"{paragraph}.")


if __name__ == '__main__':
    app()
