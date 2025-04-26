# analysis.py

def analyze_taps(taps):
    """Simple analysis placeholder."""
    if not taps:
        return None
    intervals = [taps[i+1] - taps[i] for i in range(len(taps)-1)]
    avg_interval = sum(intervals) / len(intervals) if intervals else 0
    return {
        "number_of_taps": len(taps),
        "average_interval_sec": avg_interval
    }
