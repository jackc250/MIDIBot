from __future__ import annotations
from typing import List, Tuple
import random

def pattern_to_hits(pattern: str, steps_per_beat: int = 4) -> List[float]:
    """Convert a pattern string like 'x--x--x-' to onset times (in beats).
    'x' = hit, '-' = rest. steps_per_beat controls resolution.
    """
    hits = []
    for idx, ch in enumerate(pattern.strip()):
        if ch.lower() == 'x':
            hits.append(idx / steps_per_beat)
    return hits

def humanize_timings(times: List[float], timing_jitter: float = 0.02, seed: int | None = None) -> List[float]:
    """Add small random timing offsets (in beats) to make it human-ish."""
    rng = random.Random(seed)
    return [t + rng.uniform(-timing_jitter, timing_jitter) for t in times]
