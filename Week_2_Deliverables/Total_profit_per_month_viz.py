import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Week_2_Deliverables/company_sales_data.csv')

# line plot of total profit by month
plt.plot(data['month_number'], data['total_profit'], marker = 'o')
plt.title('Total Profit by Month')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.show()
