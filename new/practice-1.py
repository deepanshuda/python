import pandas as pd

filename = "chicago.csv"

df = pd.read_csv(filename)

df['Start Time'] = pd.to_datetime(df['Start Time'])

df['hour'] = df['Start Time'].dt.hour

# print(df['hour'].isnull().sum().sum())

popular_hour = df['hour'].value_counts().idxmax()

popular_hour_1 = df['hour'].mode()[0]

# print(df.head())
# print('\n')
# print(popular_hour_1)
print(df['User Type'].value_counts())