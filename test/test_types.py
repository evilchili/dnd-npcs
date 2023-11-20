from language import types


def test_subclassing():

    class akak(types.Language):
        clicks = types.WeightedSet(("k'", 1.0),)

        def get_grapheme_click(self) -> str:
            return self.clicks.random()

    ak = akak(
        name='ClickSpeak',
        vowels=types.WeightedSet(('a', 1.0),),
        consonants=types.WeightedSet(),
        prefixes=None,
        suffixes=None,
        rules=set(),
        minimum_grapheme_count=2,
        syllables=types.SyllableSet((types.Syllable('vowel,click'), 1.0),),
    )
    assert list(ak.word(2)) == ["ak'", "ak'"]
