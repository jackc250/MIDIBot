from __future__ import annotations
import re
from typing import Iterable, List

NOTE_TO_SEMITONE = {
    'C': 0, 'C#': 1, 'Db': 1,
    'D': 2, 'D#': 3, 'Eb': 3,
    'E': 4, 'Fb': 4, 'E#': 5,
    'F': 5, 'F#': 6, 'Gb': 6,
    'G': 7, 'G#': 8, 'Ab': 8,
    'A': 9, 'A#': 10, 'Bb': 10,
    'B': 11, 'Cb': 11, 'B#': 0,
}

def note_to_midi(note: str) -> int:
    """Convert note like 'C4', 'F#3', 'Bb2' to MIDI number (C4 = 60)."""
    m = re.fullmatch(r"([A-Ga-g])([#b]?)(-?\d+)", note.strip())
    if not m:
        raise ValueError(f"Invalid note format: {note}")
    letter = m.group(1).upper() + m.group(2)
    octave = int(m.group(3))
    semitone = NOTE_TO_SEMITONE[letter]
    return (octave + 1) * 12 + semitone

def midi_to_note(number: int) -> str:
    if not (0 <= number <= 127):
        raise ValueError("MIDI number must be in 0..127")
    octave = number // 12 - 1
    semitone = number % 12
    names = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    return f"{names[semitone]}{octave}"

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

def quantize(values: Iterable[float], grid: float) -> List[float]:
    """Snap each value to nearest multiple of grid."""
    return [round(v / grid) * grid for v in values]
