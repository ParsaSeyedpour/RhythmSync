import numpy as np

def analyze_taps(taps):
    """
    Analyze tapping data.
    
    taps: list of tap timestamps (seconds)
    
    Returns a dictionary with statistics.
    """
    if len(taps) < 2:
        return {"error": "Not enough taps to analyze."}
    
    # Calculate Inter-Tap Intervals (ITI)
    itis = np.diff(taps)  # difference between consecutive taps
    
    mean_iti = np.mean(itis)
    std_iti = np.std(itis)

    analysis = {
        "number_of_taps": len(taps),
        "mean_ITI_sec": round(mean_iti, 4),
        "std_ITI_sec": round(std_iti, 4),
    }

    return analysis

def print_analysis(analysis_result):
    """Nicely print the analysis result."""
    if "error" in analysis_result:
        print("Analysis Error:", analysis_result["error"])
    else:
        print("\n--- Tap Analysis ---")
        print(f"Number of Taps        : {analysis_result['number_of_taps']}")
        print(f"Mean ITI (seconds)    : {analysis_result['mean_ITI_sec']}")
        print(f"ITI Standard Deviation: {analysis_result['std_ITI_sec']}")
        print("----------------------\n")
