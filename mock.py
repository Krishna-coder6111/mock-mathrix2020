#population.csv for total population per coordinate
#coviddataset.csv for
#ideas:
#covid cases per date
#covid cases per age (scatter plot)
#stream plot for spread
#multiplot for showing spread per day . cases/pop
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
with open('Population2.csv', 'r') as f:
      obj = csv.reader(f)
      rl=[]
      for i in obj:
            if i!=['','','']:
                  rl.append(i)
      X, Y, Z = [], [], []
      for i,row in enumerate(rl):
            xstring = row[0]
            ystring = row[1]
            zstring= row[2]
            xdata = float(int(xstring))
            ydata = float(int(ystring))
            zdata = float(int(zstring))
            X.append(xdata)
            Y.append(ydata)
            Z.append(zdata)
ax.scatter3D(X,Y,Z)
wf.set_title('Example 1') 
plt.show()
#change scatter3d to somethinelse like wf
#removed heade

      
      
