from npc.languages.base import BaseLanguage
import random


class Lizardfolk(BaseLanguage):

    vowels = []
    consonants = []
    affixes = []

    syllable_template = ()
    syllable_weights = []

    family = [
        'sweet', 'floral', 'fruity', 'sour', 'fermented', 'green', 'vegetal', 'old',
        'roasted', 'spiced', 'nutty', 'cocoa', 'pepper', 'pungent', 'burnt', 'carmelized',
        'raw', 'rotting', 'dead', 'young',
    ]

    scents = [
        'honey', 'caramel', 'maple syrup', 'molasses', 'dark chocolate', 'chocolate', 'almond',
        'hazelnut', 'peanut', 'clove', 'cinnamon', 'nutmeg', 'anise', 'malt', 'grain', 'roast',
        'smoke', 'ash', 'acrid', 'rubber', 'skunk', 'petroleum', 'medicine', 'salt', 'bitter',
        'phrenolic', 'meat', 'broth', 'animal', 'musty', 'earth', 'mould', 'damp', 'wood', 'paper',
        'cardboard', 'stale', 'herb', 'hay', 'grass', 'peapod', 'whisky', 'wine', 'malic',
        'citric', 'isovaleric', 'butyric', 'acetic', 'lime', 'lemon',
        'orange', 'grapefruit', 'pear', 'peach', 'apple', 'grape', 'pineapple', 'pomegranate',
        'cherry', 'coconut', 'prune', 'raisin', 'strawberry', 'blueberry', 'raspberry',
        'blackberry', 'jasmine', 'rose', 'camomile', 'tobacco',
    ]

    nicknames = []

    def person(self):
        return(
            random.choice(self.family),
            '-'.join([
                random.choice(self.scents),
                random.choice(self.scents),
            ]),
        )
