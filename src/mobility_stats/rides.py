import csv
import os
from collections import defaultdict


def load_rides(p: str) -> list[dict[str, object]]:
    """Load ride data from a CSV file."""
    x = []
    if os.path.exists(p) == False:
        raise FileNotFoundError(f"Could not find file: {p}")
    with open(p, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for a in r:
            a.copy()
            x.append(
                {
                    "ride_id": a["ride_id"],
                    "start_station": a["start_station"],
                    "end_station": a["end_station"],
                    "duration_min": float(a["duration_min"]),
                    "rider_type": a["rider_type"],
                }
            )
    return x


def average_duration(a):
    """Return the average ride duration in minutes."""
    if len(a) == 0:
        return 0.0
    b = 0.0
    for c in a:
        b += c["duration_min"]
    return b / len(a)


def count_by_rider_type(a):
    """Count rides for each rider type."""
    b = defaultdict(int)
    for c in a:
        b[c["rider_type"]] += 1
    return dict(b)


def busiest_start_station(a):
    """Return the start station with the most rides."""
    if a == None:
        raise ValueError("rides must not be None")
    if len(a) == 0:
        raise ValueError("rides must not be empty")
    b = {}
    for c in a:
        d = c["start_station"]
        b[d] = b.get(d, 0) + 1
    return max(b, key=b.get)


def filter_long_rides(a, b=30):
    """Return all rides with duration greater than or equal to b minutes."""
    l = []
    for c in a:
        if c["duration_min"] >= b:
            l.append(c)
    return l
