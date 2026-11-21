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

    print("empty")
    print(dataset.isnull().sum())
    
    dataset = dataset.drop_duplicates()
    dataset = dataset.bfill()
    return(dataset)




#gets rid of febuary 29 in data that has it 

def leap_del(data_set):
    leap_del_2024 = data_set.copy()
    for t in range(0, 24):
        dt = f"2024-02-29 {t}:00"
        if dt in leap_del_2024['DT_MST'].values:
            row_idx = leap_del_2024[leap_del_2024['DT_MST'] == dt].index
            leap_del_2024 = leap_del_2024.drop(row_idx)
            leap_del_2024 = leap_del_2024.reset_index(drop=True)      
    return(leap_del_2024)




# convers form hours to day
def to_day(dataset):
    s = 0
    e = 24
    count = 1
    days_power = {'Days': [], 'Calgary': [], 'Central': [], 'Edmonton': [], 'Northeast': [], 'Northwest': [], 'South': []}
    regs = ['Calgary', 'Central', 'Edmonton', 'Northeast', 'Northwest', 'South']
    while s < len(dataset):
        date = dataset['DT_MST'].iloc[s].split()[0]
        days_power['Days'].append(date)
        for reg in regs:
            result = dataset[reg].iloc[s:e].sum()
            days_power[reg].append(float(result))
        e += 24
        s += 24
        count += 1
            
    return pd.DataFrame(days_power)




#for part 3 
def day_choice(sep):
    day_choice = input(f'Do you want to convert to usage by {sep}?(yes/no)')
    while day_choice.lower() != 'yes' and day_choice.lower() != 'no':
        print('invalid choice please enter yes or no')
        day_choice = input(f'Do you want to convert to usage by {sep}?(yes/no)')
    return(day_choice)



#part 2
def region_stats(dataset, region):
    average = np.mean(dataset[region])
    minimum = np.min(dataset[region])
    maximum = np.max(dataset[region])
    return (average, minimum, maximum)




#part 4 

def calculate_metric(filtered_data, region, metric):
    values = filtered_data[region]
    if metric == 'average':
        results = np.mean(values)
    elif metric == 'minimum':
        results = np.min(values)
    elif metric == 'maximum':
        results = np.max(values)
    else:
        results = np.sum(values)
    return(results)






def time_split(dataset, hours, data_year):
    if hours == True:
        from PP3_Functions import to_day
        datasetcopy = dataset.copy() 
        datasetcopy = to_day(datasetcopy)
    else:
        datasetcopy = dataset.copy()

    valid_days = datasetcopy['Days'].tolist()

    start = input(f'Enter the starting range date.({data_year}-01-01)')
    while start not in valid_days:
        print('Invalid starting point')
        start = input(f'Enter the starting range date.({data_year}-01-01)')

    end_date = input(f'Enter the ending range date.({data_year}-01-01)')
    while end_date not in valid_days or valid_days.index(end_date) < valid_days.index(start):
        print('Invalid ending point')
        end_date = input(f'Enter the ending range date.({data_year}-01-01)')  
            
                    
    starting_row = valid_days.index(start)
    ending_row = valid_days.index(end_date)
    restricted_data = datasetcopy.iloc[starting_row : ending_row + 1]
    return(restricted_data, start, end_date)



            
        