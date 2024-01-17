import numpy as np
import pandas as pd
import tsfel


def segment_time_series(time_series, window_length, step):
    if step > window_length / 2:
        raise ValueError("Step size more than half of the window length is not allowed.")

    segments = []
    for start in range(0, len(time_series) - window_length + 1, step):
        end = start + window_length
        segment = time_series[start:end]
        segments.append(segment)

    return pd.DataFrame(segments).transpose()


# Example usage:
time_series = np.random.randn(100)  # Example time series data
window_length = 10
step = 5

segmented_data = segment_time_series(time_series, window_length, step)
print(segmented_data)


for segment in range(segmented_data.shape[1]):
    print(tsfel.autocorr(segmented_data[segment]))