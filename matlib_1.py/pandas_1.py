import pandas as pd

data = {
    'cars': [5, 4, 3, 7],  # series
    'boats': [2, 6, 0, 2]  # series
}

vehicles = pd.DataFrame(data, index=['Peter', 'Sara', 'Ali', 'John'])
print(vehicles.info())
print(vehicles.loc['Ali'])
print(vehicles.shape)