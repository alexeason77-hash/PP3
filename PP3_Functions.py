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
    dataset.head()

    print(dataset.info())

    print("empty")
    print(dataset.isnull().sum())
    
    dataset.drop_duplicates(inplace=True)
    dataset.fillna(dataset.mean(numeric_only=True), inplace = True)
    return(dataset)




#gets rid of febuary 29 in data that has it 


#def leap_del(data_set):
    leap_del_2024 = data_set.copy()
    for t in range(0, 24):
        dt = f"2024-02-29 {t}:00"
        if dt in leap_del_2024['DT_MST'].values:
            row_num = leap_del_2024['DT_MST'].tolist().index(dt)
            leap_del_2024 = leap_del_2024.drop(leap_del_2024.index[row_num])
    return(leap_del_2024)


def leap_del(data_set):
    leap_del_2024 = data_set.copy()
    for t in range(0, 24):
        dt = f"2024-02-29 {t}:00"
        if dt in leap_del_2024['DT_MST'].values:
            row_idx = leap_del_2024[leap_del_2024['DT_MST'] == dt].index
            leap_del_2024 = leap_del_2024.drop(row_idx)
    return(leap_del_2024)





def to_day(dataset):
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