import pytest
from staff import Duration, Tempo
from staff.patterns import DurationPattern


@pytest.fixture
def simple_pattern():
    return DurationPattern(
        [
            Duration(8, is_rest=True),
            Duration(8),
            Duration(8),
            Duration(8),
            Duration(2),
        ]
    )


def test_length(simple_pattern):
    assert len(simple_pattern) == 5


def test_append_prepend(simple_pattern):
    assert len(simple_pattern.append(Duration(1, is_rest=True))) == 6
    assert len(simple_pattern.prepend(Duration(1, is_rest=True))) == 6


def test_retrograde(simple_pattern):
    for idx, dur in enumerate(simple_pattern.retrograde()):
        assert dur == simple_pattern[-(idx + 1)]


def test_prolate(simple_pattern):
    tempo = Tempo(60)
    for factor in [0.5, 2]:
        assert (
            simple_pattern.milliseconds(tempo)
            == simple_pattern.prolate(factor).milliseconds(tempo) / factor
        )


def test_rotate(simple_pattern):
    assert simple_pattern[0] == simple_pattern.rotate(1)[-1]
    assert simple_pattern[0] == simple_pattern.rotate(2)[-2]
    assert simple_pattern[0] == simple_pattern.rotate(-1)[1]
