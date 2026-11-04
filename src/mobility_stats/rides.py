import csv
import os
from collections import defaultdict


def load_rides(path: str) -> list[dict[str, object]]:
    """Load ride data from a CSV file."""
    data = []
    if os.path.exists(path) == False:
        raise FileNotFoundError(f"Could not find file: {path}")
    with open(path, newline="", encoding="utf-8") as file:
        r = csv.DictReader(file)
        for rides in r:
            rides.copy()
            data.append(
                {
                    "ride_id": rides["ride_id"],
                    "start_station": rides["start_station"],
                    "end_station": rides["end_station"],
                    "duration_min": float(rides["duration_min"]),
                    "rider_type": rides["rider_type"],
                }
            )
    return data


def average_duration(rides):
    """Return the average ride duration in minutes."""
    if len(rides) == 0:
        return 0.0
    total_duration = sum(ride["duration_min"] for ride in rides)
    return total_duration / len(rides)


def count_by_rider_type(rides):
    """Count rides for each rider type."""
    station_counts = defaultdict(int)
    for ride in rides:
        station_counts[ride["rider_type"]] += 1
    return dict(station_counts)


def busiest_start_station(rides):
    """Return the start station with the most rides."""
    if rides == None:
        raise ValueError("rides must not be None")
    if len(rides) == 0:
        raise ValueError("rides must not be empty")
    station_counts = {}
    for ride in rides:
        start_location = ride["start_station"]
        station_counts[start_location] = station_counts.get(start_location, 0) + 1
    return max(station_counts, key=station_counts.get)


def filter_long_rides(rides, min_duration=30):
    """Return all rides with duration greater than or equal to min_duration minutes."""
    longest_ride = []
    for ride in rides:
        if ride["duration_min"] >= min_duration:
            longest_ride.append(ride)
    return longest_ride
