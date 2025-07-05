# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Staff is a Python toolbox for computer-assisted composition. It provides utilities for composers working with algorithmic and computer-aided music composition, integrating with libraries like Abjad, SCAMP, and Mido.

## Development Commands

### Code Quality & Formatting
```bash
make checks        # Run all checks (formatting, linting, type checking)
make black-fix     # Auto-format code
make isort-fix     # Auto-sort imports
make mypy          # Type checking
make ruff          # Linting
```

### Testing
```bash
make tests         # Run all tests (doctests + unit tests with coverage)
make tests-report  # Generate HTML coverage report
```

### Build & Release
```bash
make build         # Full build (checks + tests + package)
make package       # Build distribution packages
```

## Architecture

### Core Modules

1. **Musical Primitives** (`src/staff/`)
   - `Duration`: Musical time representation with arithmetic operations
   - `Pitch`: Frequency/MIDI pitch representations  
   - `Tempo`, `Tuplet`, `Cents`: Supporting musical concepts
   - All use frozen dataclasses with total ordering

2. **Patterns** (`src/staff/patterns/`)
   - `DurationPattern`: Immutable duration collections
   - Base pattern class for common functionality

3. **Orchestration** (`src/staff/orchestration/`)
   - `Instrument`: Musical instruments with ranges and articulations
   - `VoicedPitch`, `VoicedChord`: Pitch-instrument associations
   - `voice_pitches()`, `find_all_voicings()`: Voicing algorithms
   - SATB ensemble support with proper voice ordering

4. **Database** (`src/staff/db/`)
   - SQLite persistence for instruments/articulations
   - Instrument packs (e.g., BBC Symphony Orchestra)
   - Environment variable: `STAFF_DB_PATH`

### Key Design Patterns
- Immutable value objects using `@dataclass(frozen=True)`
- Rich operator overloading for musical operations
- Strong typing throughout
- Domain-driven design with musical concepts as first-class objects

## Testing Guidelines

- Tests are in `tests/` directory
- Use pytest with doctest support
- Doctests use NORMALIZE_WHITESPACE option
- Run a single test: `pytest tests/test_specific.py::test_function`

## Important Notes

- Package name on PyPI: `inegm.staff`
- Python >= 3.7 required
- Empty requirements.txt - dependencies managed dynamically
- Entry point: `staff` command-line tool
- Documentation: https://inegm.github.io/staff/