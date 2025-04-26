import time
import csv

class TapRecorder:
    def __init__(self):
        self.taps = []
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def record_tap(self):
        if self.start_time is not None:
            tap_time = time.time() - self.start_time
            self.taps.append(tap_time)
            print(f"Tap recorded at {tap_time:.4f} seconds")

    def save_to_csv(self, filepath):
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Tap Number", "Time Since Start (s)"])
            for idx, tap in enumerate(self.taps):
                writer.writerow([idx + 1, tap])
        print(f"Taps saved to {filepath}")
