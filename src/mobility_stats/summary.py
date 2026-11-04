from mobility_stats.rides import average_duration, busiest_start_station, count_by_rider_type


def build_summary(a):
    """Build a compact dictionary with headline statistics."""
    b = {
        "ride_count": len(a),
        "average_duration": average_duration(a),
        "rider_types": count_by_rider_type(a),
    }
    if a:
        b["busiest_start_station"] = busiest_start_station(a)
    else:
        b["busiest_start_station"] = None
    return b


def format_summary(a):
    """Create a human-readable text summary."""
    title = "Mobility summary"
    line1 = f"Rides: {a['ride_count']}"
    line2 = f"Average duration: {a['average_duration']:.1f} min"
    line3 = f"Busiest start: {a['busiest_start_station']}"
    return title + "\n" + line1 + "\n" + line2 + "\n" + line3
