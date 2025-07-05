"""Stub file for staff.orchestration.ensemble module."""

from __future__ import annotations
from typing import List
from enum import Enum
from .instrument import Instrument
from .voicing import VoicedChord
from ..pitch import MIDIPitch

class SATBRole(Enum):
    SOPRANO: str
    ALTO: str
    TENOR: str
    BASS: str
    
    def __lt__(self, other: SATBRole) -> bool: ...

class SATBEnsembleInstrument:
    instrument: Instrument
    role: SATBRole
    
    def __init__(self, instrument: Instrument, role: SATBRole) -> None: ...
    
    def __lt__(self, other: SATBEnsembleInstrument) -> bool: ...

class SATBEnsemble:
    name: str
    instruments: List[SATBEnsembleInstrument]
    description: str
    category: str
    
    def __init__(
        self,
        name: str,
        instruments: List[SATBEnsembleInstrument],
        description: str = "",
        category: str = "Default",
    ) -> None: ...
    
    def add_instrument(self, instrument: Instrument, role: str) -> SATBEnsemble: ...

class Ensemble:
    name: str
    instruments: List[Instrument]
    description: str
    category: str
    
    def __init__(
        self,
        name: str,
        instruments: List[Instrument],
        description: str = "",
        category: str = "Default",
    ) -> None: ...
    
    def add_instrument(self, instrument: Instrument) -> Ensemble: ...
    def voice(self, pitches: List[MIDIPitch], openness: float = 0.5) -> VoicedChord: ...
    def voice_lead(self, voicing: VoicedChord, target: List[MIDIPitch]) -> VoicedChord: ...