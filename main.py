"""Example usage of the composer package.

Creates a simple groove:
  - C minor pentatonic bass ostinato
  - Backbeat snare (channel 9 / track 1 as 'drums')
  - Arpeggiated Cm7 chord tones
"""
from composer import note_to_midi, scale, chord, pattern_to_hits, humanize_timings
from composer import MidiWriter, NoteEvent, ChordEvent

def build_example(filename: str = 'outputs/example_groove.mid'):
    writer = MidiWriter(num_tracks=2, tempo=100)

    # Bass: C minor pentatonic around C2
    bass_scale = scale('C2', mode='pentatonic_minor', octaves=1)
    bass_pattern = [0, 2, 3, 4]  # pick some degrees
    time = 0.0
    events = []
    for bar in range(4):
        for deg in bass_pattern:
            pitch = bass_scale[deg]
            events.append(NoteEvent(pitch=pitch, start=time, duration=1.0, velocity=95, channel=0, track=0))
            time += 1.0
    writer.add_notes(events)

    # Drums: Kick on 1 & 3, Snare on 2 & 4 (use channel 9 for GM drums)
    drum_events = []
    kick = 36  # Bass Drum 1
    snare = 38 # Acoustic Snare
    for bar in range(4):
        bar_start = bar*4
        drum_events.extend([
            NoteEvent(kick,  bar_start + 0.0, 0.25, 100, channel=9, track=1),
            NoteEvent(snare, bar_start + 2.0, 0.25, 105, channel=9, track=1),
            NoteEvent(kick,  bar_start + 3.0, 0.25, 100, channel=9, track=1),
        ])
    writer.add_notes(drum_events)

    # Harmony: Cm7 arpeggio pattern
    cm7 = chord('C4', 'min7')
    arp_events = []
    t = 0.0
    for bar in range(4):
        for step in range(8):  # 8th-note arpeggio
            pitch = cm7[step % len(cm7)]
            arp_events.append(NoteEvent(pitch, start=t+step*0.5, duration=0.45, velocity=80, channel=1, track=0))
        t += 4.0
    writer.add_notes(arp_events)

    writer.write(filename)
    return filename

if __name__ == '__main__':
    out = build_example()
    print('Wrote', out)
