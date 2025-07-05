"""Stub file for staff package."""

__version__: str

# Submodule exports
from . import duration as duration
from . import pitch as pitch

# Direct exports from submodules
from .duration import Duration as Duration, Tempo as Tempo, Tuplet as Tuplet
from .patterns import DurationPattern as DurationPattern
from .pitch import (
    Cents as Cents,
    Diapason as Diapason,
    Frequency as Frequency,
    MIDIBend as MIDIBend,
    MIDIPitch as MIDIPitch,
)