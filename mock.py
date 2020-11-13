#population.csv for total population per coordinate
#coviddataset.csv for
#ideas:
#covid cases per date
#covid cases per age (scatter plot)
#stream plot for spread
#multiplot for showing spread per day . cases/pop
import csv
from mpl_toolkits.mplot3d import axes3d 
from matplotlib import pyplot 

def csvlist(reading):
      l=[]
      for i in reading:
            if i !=[]:
                  l.append(l)
      return l
with open('Population.csv','r') as f2:
      reading2=csv.reader(f2)
      pop=csvlist(reading2) # [x,y,pop]
      
from mpl_toolkits.mplot3d import axes3d 
from matplotlib import pyplot  
##import numpy as geek 
##  
##arr = geek.array([1, 2, 3, 4]) 
##  
##gfg = arr.ndim 
#got ndim errors while trying to execute with population.csv
print (gfg)
# creating the visualiztion 
fig = pyplot.figure() 
wf = fig.add_subplot(111, projection='3d') 
x, y, z = geek.(array[[1,2,3],[3,4,5],[4,5,6]])
wf.plot_wireframe(x,y,z, rstride=2,  
                  cstride=2,color='green') 
   
# displaying the visualization 
wf.set_title('Example 1') 
pyplot.show() 
 

      
      
