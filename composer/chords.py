from __future__ import annotations
from typing import List

from .midi_utils import note_to_midi

CHORDS = {
    'maj':  [0,4,7],
    'min':  [0,3,7],
    'dim':  [0,3,6],
    'aug':  [0,4,8],
    'sus2': [0,2,7],
    'sus4': [0,5,7],

    'maj7': [0,4,7,11],
    'min7': [0,3,7,10],
    '7':    [0,4,7,10],
    'dim7': [0,3,6,9],
    'm7b5': [0,3,6,10],
    'minmaj7': [0,3,7,11],
}

def chord(root: str | int, quality: str = 'maj', inversion: int = 0) -> List[int]:
    """Return MIDI numbers for a chord. Supports inversions >= 0."""
    if isinstance(root, int):
        root_midi = root
    else:
        root_midi = note_to_midi(root)

    intervals = CHORDS[quality][:]
    notes = [root_midi + i for i in intervals]

    # Apply inversion by raising lowest notes by octaves
    for _ in range(inversion):
        lowest = notes.pop(0)
        notes.append(lowest + 12)
    return notes
