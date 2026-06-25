# Goal : to analyze a small, publicly available dataset using pandas:
# to explore the data, print first few rows, check data types, and compute summary statistics (mean, median, standard deviation).
# Dataset gotten from : https://www.kaggle.com/datasets/whenamancodes/student-dataset
import pandas as pd
data = pd.read_csv('Week_3_Deliverables/data/student_dataset_10000_rows.csv')
# print first few rows.
print(f'First few rows : \n {data.head()}')
# checking data types
print(f'Data Types : \n {data.dtypes}')
# Summary stats(mean, median, standard deviation).
print(f'Summary Statistics : \n {data.describe()}')