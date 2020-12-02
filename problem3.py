import matplotlib.pyplot as plt
import statsmodels.api as stats
import pandas as pd
import numpy as np

data = pd.read_csv("NYC_Bicycle_Counts_2016_Corrected.csv")
total = list(data['Total'])
total = [i.replace(",","") for i in total]
for i in range(0, len(total)):
    total[i] = float(total[i])
precipitation = list(data['Precipitation'])
for i in range(len(precipitation)):
    if precipitation[i] == 'T':
        precipitation[i] = 0
precipitation[3] = 0.47
for i in range(0, len(precipitation)):
    precipitation[i] = float(precipitation[i])

plt.scatter(total,precipitation,color="blue")
plt.title('Precipitation vs Number of Bicyclist')
plt.xlabel('Bicyclist')
plt.ylabel('Precipitation')
plt.grid(True)
plt.show()

Y = np.array(precipitation).reshape((-1, 1))
X = total

X1 = stats.add_constant(X)
model = stats.OLS(Y, X1)
results = model.fit()
print("params: \n", results.params)
print("R squared:", results.rsquared)

