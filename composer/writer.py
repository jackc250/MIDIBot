from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, List, Sequence

from midiutil import MIDIFile

@dataclass
class NoteEvent:
    pitch: int            # MIDI note number 0..127
    start: float          # in beats
    duration: float       # in beats
    velocity: int = 100   # 0..127
    channel: int = 0
    track: int = 0

@dataclass
class ChordEvent:
    pitches: Sequence[int]
    start: float
    duration: float
    velocity: int = 92
    channel: int = 0
    track: int = 0

class MidiWriter:
    def __init__(self, num_tracks: int = 1, tempo: int = 120):
        self.midi = MIDIFile(numTracks=num_tracks, adjust_origin=False)
        for t in range(num_tracks):
            self.midi.addTempo(t, 0, tempo)

    def add_notes(self, events: Iterable[NoteEvent]) -> None:
        for e in events:
            self.midi.addNote(e.track, e.channel, e.pitch, e.start, e.duration, e.velocity)

    def add_chords(self, events: Iterable[ChordEvent]) -> None:
        for e in events:
            for p in e.pitches:
                self.midi.addNote(e.track, e.channel, int(p), e.start, e.duration, e.velocity)

    def write(self, path: str) -> None:
        import os
        os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
        with open(path, 'wb') as f:
            self.midi.writeFile(f)
