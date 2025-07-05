"""Stub file for staff.db.instruments module."""

from typing import Optional
from ..orchestration.instrument import Instrument

# Import DB_PATH from parent module
from . import DB_PATH

def create_tables(db_path: str = ...) -> None: ...

def load_instrument(
    name: str,
    db_path: str = ...,
    category: str = "Default",
) -> Instrument: ...

def store_instrument(
    instrument: Instrument,
    db_path: str = ...,
) -> None: ...

def delete_instrument(
    name: str,
    db_path: str = ...,
    category: str = "Default",
) -> None: ...