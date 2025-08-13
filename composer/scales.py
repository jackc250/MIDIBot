from __future__ import annotations
from typing import List

from .midi_utils import note_to_midi

MODES = {
    'ionian':      [0,2,4,5,7,9,11],
    'dorian':      [0,2,3,5,7,9,10],
    'phrygian':    [0,1,3,5,7,8,10],
    'lydian':      [0,2,4,6,7,9,11],
    'mixolydian':  [0,2,4,5,7,9,10],
    'aeolian':     [0,2,3,5,7,8,10],
    'locrian':     [0,1,3,5,6,8,10],
    'major':       [0,2,4,5,7,9,11],
    'minor':       [0,2,3,5,7,8,10],
    'harmonic_minor': [0,2,3,5,7,8,11],
    'melodic_minor':  [0,2,3,5,7,9,11],
    'pentatonic_major': [0,2,4,7,9],
    'pentatonic_minor': [0,3,5,7,10],
    'chromatic': list(range(12)),
}

def scale(root: str | int, mode: str = 'major', octaves: int = 1, start_octave: int | None = None) -> List[int]:
    """Return MIDI numbers for a scale starting at root across octaves.
    If root is a note name (e.g., 'C4'), use that; if it's an int, treat as MIDI number.
    If start_octave is given and root is a letter like 'C', use it for base octave.
    """
    if isinstance(root, int):
        root_midi = root
    else:
        # Allow 'C' without octave if start_octave provided
        if len(root) in (1,2) and start_octave is not None:
            root = f"{root}{start_octave}"
        root_midi = note_to_midi(root)

    intervals = MODES[mode]
    out = []
    for o in range(octaves):
        base = root_midi + 12*o
        for i in intervals:
            out.append(base + i)
    return out
