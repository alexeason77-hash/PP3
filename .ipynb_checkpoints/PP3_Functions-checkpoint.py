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

# cleans the input data
def data_clean(data_file):

    dataset = pd.read_csv(data_file)

    print(dataset.info())

    print("empty")
    print(dataset.isnull().sum())
    
    dataset.drop_duplicates(inplace=True)
    dataset.fillna(dataset.mean(numeric_only=True), inplace = True)
    return(dataset)
