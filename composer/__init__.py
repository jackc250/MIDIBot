"""composer: a tiny toolkit for algorithmic MIDI composition.

Modules:
  - midi_utils: note name parsing, scales, helpers
  - scales: scale generation utilities
  - chords: chord formulas and builders
  - rhythm: rhythm pattern utilities and humanization
  - writer: MIDI writer built on midiutil
"""

from .midi_utils import note_to_midi, midi_to_note, clamp, quantize
from .scales import scale, MODES
from .chords import chord, CHORDS
from .rhythm import pattern_to_hits, humanize_timings
from .writer import MidiWriter, NoteEvent, ChordEvent
