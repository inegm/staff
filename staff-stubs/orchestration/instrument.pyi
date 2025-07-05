"""Stub file for staff.orchestration.instrument module."""

from __future__ import annotations
from typing import List
from ..pitch import MIDIPitch

class Articulation:
    name: str
    key_switch: MIDIPitch
    abbreviation: str
    description: str
    
    def __init__(
        self,
        name: str,
        key_switch: MIDIPitch,
        abbreviation: str = "",
        description: str = "",
    ) -> None: ...

class InstrumentRange:
    bottom: MIDIPitch
    top: MIDIPitch
    
    def __init__(self, bottom: MIDIPitch, top: MIDIPitch) -> None: ...

class Instrument:
    name: str
    section: str
    range: InstrumentRange
    articulations: List[Articulation]
    is_continuous: bool
    abbreviation: str
    category: str
    description: str
    
    def __init__(
        self,
        name: str,
        section: str,
        range: InstrumentRange,
        articulations: List[Articulation],
        is_continuous: bool = False,
        abbreviation: str = "",
        category: str = "Default",
        description: str = "",
    ) -> None: ...
    
    def __eq__(self, other: object) -> bool: ...
    def __gt__(self, other: Instrument) -> bool: ...
    def __lt__(self, other: Instrument) -> bool: ...
    def __ge__(self, other: Instrument) -> bool: ...
    def __le__(self, other: Instrument) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    
    def in_range(self, pitch: MIDIPitch) -> bool: ...
    def to_range(self, pitch: MIDIPitch, close_to: MIDIPitch) -> MIDIPitch: ...
    def get_articulation(self, name: str) -> Articulation: ...