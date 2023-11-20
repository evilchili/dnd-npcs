import pytest
from language.types import WeightedSet
from language.languages.common import common


@pytest.mark.parametrize('values,expected_members,expected_weights', [
    ((('foo', 1.0), ('bar', 0.5)), ('foo', 'bar'), (1.0, 0.5))
])
def test_WeightedSet(values, expected_members, expected_weights):

    print(*values)
    ws = WeightedSet(*values)
    assert ws.members == expected_members
    assert ws.weights == expected_weights
    assert ws.random()


def test_common():
    for i in range(50000):
        assert common.word()
