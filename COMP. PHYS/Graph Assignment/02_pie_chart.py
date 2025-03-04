# 2. Pie Chart
# Question: Generate a pie chart showing the market share of 
# different smartphone
# brands. Use the dataset below:
# brands = [’Apple’, ’Samsung’, ’Huawei’, ’Xiaomi’, ’OnePlus’]
# market_share = [35, 25, 15, 15, 10]
# Expected Plot: A pie chart with each slice representing a 
# different smartphone brand and its market share.

from matplotlib import pyplot as plt
brands = ['Apple', 'Samsung', 'Huawei', 'Xiaomi', 'OnePlus']
market_share = [35, 25, 15, 15, 10]
plt.pie(market_share, labels = brands, autopct='%1.1f%%')   
plt.title('Smartphone Market Share')
plt.show()