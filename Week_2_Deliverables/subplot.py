import pandas as pd
import matplotlib.pyplot as plt
data = data = pd.read_csv('Week_2_Deliverables/company_sales_data.csv')
# create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (8, 6))
#plot for bathing soap
ax1.plot(data['month_number'], data['bathingsoap'], color = 'blue',marker = 'o', linewidth = 2)
ax1.set_title('Bathing Soap Sales per Month')
ax1.set_ylabel('Units Sold')

#Facewash sales
ax2.plot(data['month_number'], data['facewash'], color='red', marker='o', linewidth=2)
ax2.set_title('Facewash Sales per Month')
ax2.set_xlabel('Month Number')
ax2.set_ylabel('Units Sold')

plt.tight_layout()
plt.show()