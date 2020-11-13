#population.csv for total population per coordinate
#coviddataset.csv for
#ideas:
#covid cases per date
#covid cases per age (scatter plot)
#stream plot for spread
#multiplot for showing spread per day . cases/pop
import csv
import matplotlib.pyplot as plt

def csvlist(reading):
      l=[]
      for i in reading:
            if i !=[]:
                  l.append(l)
      return l

x=[5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]
x1=[1, 2, 3, 4, 7]
y1 = [1, 5, 8, 4, 2]

with open('coviddataset.csv','r') as f:
      reading=csv.reader(f)
      rl=csvlist(reading)
[gotinfectionday, countinfection+1day,x,y,age,diabetes,respiratory,abnormal bp,alive/dead]
with open('Population.csv','r') as f2:
      reading2=csv.reader(f2)
      pop=csvlist(reading2) # [x,y,pop]
#no. of patients per day
count=0
dayl=[]
countl=[]

for i in range(20):#354421):BRUH TOO BIG
      for j in range(len(rl[i])):
            day=rl[i][j][0]
            print(day,rl[i+1][j][0])
            if day==rl[i+1][1]:
                  print(day,rl[i+1][j][0])
                  count+=1
            else:
                  dayl.append(day)
                  countl.append(count)
print(day,rl[i+1][1])
print(dayl,countl)

plt.bar(dayl,countl)
plt.show()
 

      
