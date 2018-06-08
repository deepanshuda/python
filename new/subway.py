import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = '/Users/deepanshuagarwal/Developer/Udacity/Python/new/nyc-subway-weather.csv'
subway_df = pd.read_csv(filename)

# print(subway_df)

print("\n")

ridership = subway_df.groupby("DATEn").mean()["ENTRIESn_hourly"]
# print(ridership)

ridership.plot()