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

    Note:
        This class can be stored and retrieved from a database.
        See the documentation for the `staff.db` module for more information.

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

    # TODO: Add CC numbers for vibrato, expression, etc.

    name: str
    section: str
    range: InstrumentRange
    articulations: List[Articulation]
    is_continuous: bool = False
    abbreviation: str = ""
    category: str = "Default"
    description: str = ""

    def __repr__(self) -> str:
        """Return a string representation of the instrument."""
        return (
            f"Instrument(name='{self.name}', "
            f"category='{self.category}', "
            f"description='{self.description}')"
        )

    def in_range(self, pitch: MIDIPitch) -> bool:
        """Check if a pitch is in the instrument's range.

        Args:
            pitch: The pitch to check.

        Returns:
            True if the pitch is in the instrument's range, False otherwise.
        """
        return self.range.bottom <= pitch <= self.range.top

    def to_range(
        self,
        pitch: MIDIPitch,
        close_to: MIDIPitch,
    ) -> MIDIPitch:
        """Finds the pitch within the instrument's range, closest to another.

        Args:
            pitch: The pitch to coerce.
            close_to: A pitch close to where the resulting pitch should be.

        Returns:
            The coerced pitch.

        Raises:
            ValueError: If `close_to` is not in the instrument's range.

        Examples:
            >>> from staff import MIDIPitch
            >>> from staff.orchestration.instrument import Instrument, InstrumentRange
            >>> instrument = Instrument(
            ...     name="Violin",
            ...     section="Strings",
            ...     range=InstrumentRange(
            ...         bottom=MIDIPitch(55),
            ...         top=MIDIPitch(103),
            ...     ),
            ...     articulations=[],
            ...     is_continuous=True,
            ... )
            >>> low_e = MIDIPitch.from_string("E1")
            >>> target = MIDIPitch.from_string("E3")
            >>> target == instrument.to_range(low_e, instrument.range.bottom)
            True
        """
        if close_to > self.range.top:
            close_to = self.range.top
        elif close_to < self.range.bottom:
            close_to = self.range.bottom

        distance = abs(pitch.pitch_class - close_to.pitch_class)

        if distance == 0:
            coerced_number = close_to.number
        elif distance < (pitch.octave_divs / 2):
            coerced_number = close_to.number - distance
            if coerced_number < self.range.bottom.number:
                coerced_number = close_to.number + distance
        else:
            coerced_number = close_to.number + distance
            if coerced_number > self.range.top.number:
                coerced_number = close_to.number - distance

        return MIDIPitch(
            number=coerced_number,
            bend=pitch.bend,
            diapason=pitch.diapason,
            octave_divs=pitch.octave_divs,
        )

    def get_articulation(self, name: str) -> Articulation:
        """Get an articulation by name.

        Args:
            name: The name of the articulation.

        Returns:
            The articulation.

        Raises:
            ValueError: If the articulation does not exist.
        """
        for articulation in self.articulations:
            if articulation.name == name:
                return articulation
        raise ValueError(f"Articulation '{name}' does not exist.")
