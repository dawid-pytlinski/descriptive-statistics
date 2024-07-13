import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, mode

file_path = 'descreptive_statistics_01_IoT.xlsx'
df = pd.read_excel(file_path)

df = df.drop(columns=['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12'])
df = df.dropna()

numeric_df = df.select_dtypes(include=[np.number])

descriptive_stats = numeric_df.describe().T

mode_vals = numeric_df.mode().iloc[0]
descriptive_stats['mode'] = mode_vals

descriptive_stats['variance'] = numeric_df.var()

descriptive_stats['skewness'] = numeric_df.skew()

descriptive_stats['kurtosis'] = numeric_df.kurtosis()

descriptive_stats['coeff_of_variation'] = descriptive_stats['std'] / descriptive_stats['mean']

descriptive_stats['range'] = descriptive_stats['max'] - descriptive_stats['min']

descriptive_stats['Q1'] = numeric_df.quantile(0.25)
descriptive_stats['Q3'] = numeric_df.quantile(0.75)

print(descriptive_stats)

plt.figure(figsize=(14, 10))

variables = ['Temperature', 'Humidity', 'Light', 'CO2', 'HumidityRatio']

for i, var in enumerate(variables, 1):
    plt.subplot(2, 3, i)
    sns.boxplot(y=var, data=numeric_df)
    plt.title(f'Box plot of {var}')

plt.tight_layout()
plt.show()
