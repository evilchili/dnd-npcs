from npc import load_ancestry_pack


import logging
import os
from enum import Enum
from typing import Union

import typer
from rich import print
from rich.logging import RichHandler


from language import load_language_pack

app = typer.Typer()

app_state = {}

language_pack, supported_languages = load_language_pack()
SupportedLanguages = Enum("SupportedLanguages", ((k, k) for k in supported_languages.keys()))

ancestry_pack, supported_ancestries = load_ancestry_pack()
SupportedAncestries = Enum("SupportedAncestries", ((k, k) for k in supported_ancestries.keys()))


def get_npc(**kwargs):
    return app_state['ancestry'].NPC(language=app_state['language'], **kwargs)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    ancestry: SupportedAncestries = typer.Option(
        default="human",
        help="The ancestry to use."
    ),
    language: Union[SupportedLanguages, None] = typer.Option(
        default=None,
        help="The language to use. Will be derived from ancestry if not specified."
    ),
    verbose: bool = typer.Option(
        default=False,
        help="If True, print verbose character descriptions."
    )
):
    app_state["ancestry"] = supported_ancestries[ancestry.name]
    if language:
        app_state["language"] = supported_languages[language.name]
    else:
        app_state["language"] = None

    debug = os.getenv("NPC_DEBUG", None)
    logging.basicConfig(
        format="%(name)s %(message)s",
        level=logging.DEBUG if debug else logging.INFO,
        handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[typer])],
    )
    logging.debug(f"Loaded ancestry pack {ancestry_pack}.")
    logging.debug(f"Loaded language pack {language_pack}.")

    app_state['verbose'] = verbose

    if ctx.invoked_subcommand is None:
        return commoner()


@app.command()
def commoner() -> None:
    """
    Generate a basic NPC.
    """
    char = get_npc()
    if app_state['verbose']:
        print(char.character_sheet)
    else:
        print(char)


@app.command()
def adventurer() -> None:
    """
    Generate a basic NPC.
    """
    char = get_npc(randomize=True)
    if app_state['verbose']:
        print(char.character_sheet)
    else:
        print(char)


@app.command()
def noble() -> None:
    """
    Generate a basic NPC.
    """
    char = get_npc(randomize=True, noble=True)
    if app_state['verbose']:
        print(char.character_sheet)
    else:
        print(char)


if __name__ == '__main__':
    app()
