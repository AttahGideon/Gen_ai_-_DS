# Goal : Calculate basic statistics(Mean, Median, Mode, Standard Deviation) for each numerical feature 
# and correlation between different features in the dataset.
import pandas as pd
data = pd.read_csv('Week_3_Deliverables/data/student_dataset_10000_rows.csv')
#calculate mean, median, mode and standard deviation for each numerical feature.
print(f'Mean : \n {data.mean(numeric_only = True)}')

print(f'Median : \n {data.median(numeric_only = True)}')

print(f'Mode : \n {data.mode(numeric_only = True)}')

print(f'Standard Deviation : \n {data.std(numeric_only = True)}')

#Correlation between different features.
print(f'Correlation : \n {data.corr(numeric_only = True)}')