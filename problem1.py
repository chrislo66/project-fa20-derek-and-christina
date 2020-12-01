import pandas as pd
from matplotlib import pyplot as plt
import statistics

data = pd.read_csv('NYC_Bicycle_Counts_2016_Corrected.csv')
brooklyn = list(data['Brooklyn Bridge'])
brooklyn = [i.replace(",","") for i in brooklyn]
for i in range(0, len(brooklyn)):
    brooklyn[i] = int(brooklyn[i])
manhattan = list(data['Manhattan Bridge'])
manhattan = [i.replace(",","") for i in manhattan]
for i in range(0, len(manhattan)):
    manhattan[i] = int(manhattan[i])
williamsburg = list(data['Williamsburg Bridge'])
williamsburg = [i.replace(",","") for i in williamsburg]
for i in range(0, len(williamsburg)):
    williamsburg[i] = int(williamsburg[i])
queensboro = list(data['Queensboro Bridge'])
queensboro = [i.replace(",","") for i in queensboro]
for i in range(0, len(queensboro)):
    queensboro[i] = int(queensboro[i])
x = [0]*214
for i in range(214):
    x [i] = i+1

fig, pos = plt.subplots(2, 2)
fig.suptitle("Number of bikes in each city per day")
pos[0,0].plot(x, brooklyn, color = 'red')
pos[0,0].set_title('Brooklyn')
pos[0,0].set(xlim =(0,214), ylim=(0, 10000))
pos[0,0].set(xlabel = 'Number of Day', ylabel = 'Number of bikes')


pos[1,0].plot(x, manhattan,color = 'blue', label = 'Manhattan')
pos[1,0].set(xlim =(0,214), ylim=(0, 10000))
pos[1,0].legend(loc = 'upper right')
pos[1,0].set(xlabel = 'Number of Day', ylabel = 'Number of bikes')


pos[0,1].plot(x, williamsburg, color = 'green')
pos[0,1].set_title('Williamsburg')
pos[0,1].set(xlim =(0,214), ylim=(0, 10000))
pos[0,1].set(xlabel = 'Number of Day', ylabel = 'Number of bikes')

pos[1,1].plot(x, queensboro, color = 'black', label = 'Queensboro')
pos[1,1].set(xlim =(0,214), ylim=(0, 10000))
pos[1,1].legend(loc = 'upper right')
pos[1,1].set(xlabel = 'Number of Day', ylabel = 'Number of bikes')

plt.show()