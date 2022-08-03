from npc.generator.base import generate_npc, npc_type
from npc import languages
from rich import print

import random
import typer


app = typer.Typer()


@app.command()
def npc(ancestry=None, name=None, pronouns=None, title=None,
        nickname=None, whereabouts="Unknown", STR=None, DEX=None, CON=None,
        INT=None, WIS=None, CHA=None, randomize=False):
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
def names(ancestry=None, count=1):
    for _ in range(int(count)):
        print(npc_type(ancestry)().full_name)


@app.command()
def text(language='common', words=50):

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
    for word in [lang.word() for _ in range(int(words))]:
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
