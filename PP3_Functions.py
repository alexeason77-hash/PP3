import numpy as np
import pandas as pd
"""
Calculates the total power usage per day from an hourly dataset.

Parameters:
dataset: The 2D array containing the time and power records.

Returns:
numpy.ndarray: A 2D array formatted as [day_number, total_power]
"""
def power_h_d(dataset, reg_col):
    s = 0
    e = 24
    count = 1
    days_power = []
    while s < len(dataset):
        result = dataset[s:e, reg_col].sum()
        days_power.append([count, float(result)])
        e += 24
        s += 24
        count += 1
    return np.array(days_power)
