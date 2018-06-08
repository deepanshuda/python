import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

print(example_df)

print(example_df.groupby('even').groups)
# print(example_df.groupby(['even', 'above_three']).groups)
print(example_df.groupby('even').sum())