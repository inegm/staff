from __future__ import annotations
from dataclasses import dataclass
from typing import List

from staff import MIDIPitch


@dataclass
class Articulation:
    """An articulation of a musical instrument.

    Note:
        Some articulations change the instrument's range, such as mutes for brass
        or harmonics for strings. These range changes are not yet implemented.

    Args:
        name: The name of the articulation.
        key_switch: The key switch that triggers the articulation.
        abbreviation: The abbreviation of the articulation.
        description: The description of the articulation.
    """

    # TODO Add support for articulations that change the instrument's range.

    name: str
    key_switch: MIDIPitch
    abbreviation: str = ""
    description: str = ""


@dataclass
class InstrumentRange:
    bottom: MIDIPitch
    top: MIDIPitch


@dataclass
class Instrument:
    """A musical instrument.

    Args:
        name: The name of the instrument.
        section: The section the instrument belongs to.
        range: The range of the instrument.
        articulations: The articulations of the instrument.
        is_continuous: Whether or not the instrument is continuous (like a string
            instrument or a trombone).
        abbreviation: The abbreviation of the instrument.
        category: The category the instrument belongs to, which only serves to keep
            instruments organised. An example use would be to group by VST
            plugins.
        description: The description of the instrument.
    """

    name: str
    section: str
    range: InstrumentRange
    articulations: List[Articulation]
    is_continuous: bool = False
    abbreviation: str = ""
    category: str = "Default"
    description: str = ""

    def in_range(self, pitch: MIDIPitch) -> bool:
        """Check if a pitch is in the instrument's range.

        Args:
            pitch: The pitch to check.

        Returns:
            True if the pitch is in the instrument's range, False otherwise.
        """
        return self.range.bottom <= pitch <= self.range.top
