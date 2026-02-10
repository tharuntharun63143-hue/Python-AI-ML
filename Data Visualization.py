#data loading and print starting ten columns
import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset("titanic")
titanic.head(10)

#Histogram graph for distribution
plt.figure(figsize = (5,6))
sns.histplot(titanic['age'],kde = True,bins=30,color = 'lightgreen')
plt.title("Age ditribution of titanic passenger")
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

#Box ploat or graph 
plt.figure(figsize = (10,10))
sns.boxplot(titanic['fare'],color = 'gold')
plt.title("fare distribution of titanic passenger")
plt.xlabel('age')
plt.ylabel('fare')
plt.show()

#Scatter plot for  Correlation
plt.figure(figsize = (5,6))
sns.scatterplot(x= 'age', y = 'fare', data=titanic, hue='survived' ,palette ='coolwarm')
plt.title("Age of survived in titanic")
plt.xlabel('age')
plt.ylabel('survived')
plt.show()

#line plot
import numpy as np
import matplotlib.pyplot as plt
days = np.arange(1,9)
revenue = [100,120,130,150,200,230,180,250]
plt.figure(figsize = (7,4))
plt.plot(days, revenue, marker='o')
plt.title('Revenue trends over ten days')
plt.xlabel('days')
plt.ylabel('Revenue')
plt.show()

#Bar graph or plot
plt.figure(figsize = (8,5))
sns.barplot(x='class',y= 'fare',data=titanic,estimator='mean',ci=None,palette='pastel')
plt.title("Average fare by class")
plt.xlabel('class')
plt.ylabel('fare')

#Count plot
plt.figure(figsize = (7,4))
sns.countplot(x='sex',data=titanic,hue='survived',palette='Set2')
plt.title('Gender VS Survived count')
plt.xlabel('Sex')
plt.show()
plt.show()

#Pie chart-ratio or position
survived_count = titanic['survived'].value_counts()
plt.figure(figsize = (6,6))
plt.pie(survived_count,labels=['not survived','survived'],autopct='%1.1f%%',colors = ['lightblue','lightgrey'])
plt.title('Survived Ratio in titanic')
plt.show()

#heat map-Correlation matrices
plt.figure(figsize = (7,4))
sns.heatmap(titanic.corr(numeric_only=True),annot=True,cmap='coolwarm',fmt='.2f')
plt.title("Correlation between heatmap with the numeric features")
plt.show()
