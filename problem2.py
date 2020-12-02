import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as stats

temp_dictionary = {}
data = pd.read_csv('NYC_Bicycle_Counts_2016_Corrected.csv')
highTemp = list(data['High Temp (°F)'])
lowTemp = list(data['Low Temp (°F)'])
totalRiders = list(data['Total'])
totalRiders = [i.replace(",","") for i in totalRiders]
for i in range(0, len(totalRiders)):
    totalRiders[i] = float(totalRiders[i])

plt.scatter(highTemp,totalRiders,color="blue")
plt.title('Total Riders vs High Temp')
plt.xlabel('High Temp')
plt.ylabel('Total Riders')
plt.grid(True)
plt.show()

plt.scatter(lowTemp,totalRiders,color="red")
plt.title('Total Riders vs Low Temp')
plt.xlabel('Low Temp')
plt.ylabel('Total Riders')
plt.grid(True)
plt.show()

X = data[['High Temp (°F)','Low Temp (°F)']]
Y = totalRiders

X1 = stats.add_constant(X)
model = stats.OLS(Y, X1)
results = model.fit()
print("params: \n", results.params)
print("R squared:", results.rsquared)

