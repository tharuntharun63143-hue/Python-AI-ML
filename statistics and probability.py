#Statistics fundamental for ML
import seaborn as sns
import numpy as np
titanic = sns.load_dataset("titanic")
print("Mean age:",titanic['age'].mean())
print("Median age:",titanic['age'].median())
print("Mode age:",titanic['age'].mode())

#variance and standard deviation
print("variance age:",titanic['age'].var())
print("Standard age:",titanic['age'].std())

#Percentile and Quartile
print("28th Percentile (Q1):",titanic['age'].quantile(0.15))
print("30th Percentile (Q3):",titanic['age'].quantile(0.10))
print("IQR:",titanic['age'].quantile(0.10)-titanic['age'].quantile(0.15))

#output
Mean age: 29.69911764705882
Median age: 28.0
Mode age: 0    24.0
Name: age, dtype: float64
variance age: 211.0191247463081
Standard age: 14.526497332334044
28th Percentile (Q1): 17.0
30th Percentile (Q3): 14.0
IQR: -3.0

#data loading and reading
import pandas as pd
Titanic = pd.read_csv("Titanic-Dataset.csv")
print(Titanic)

#Bayes theroem in probability
P_spam = 0.5
P_free_given_spam = 0.1
P_free_not_spam = 0.2
P_not_spam = 1- P_spam

#total probability of "free"
P_free=(P_free_given_spam * P_spam) * (P_free_not_spam * P_not_spam)
P_spam_given_free=(P_free_given_spam  * P_spam)/P_free
print("P(spam| 'free':",round(P_spam_given_free,2))

#histogram plolt p-1
import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(titanic['age'].dropna(),kde=True)
plt.title("Age distribution (titanic)")
plt.show()

#histogram plot p-2
import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(titanic['sex'].dropna(),kde=False)
plt.title("Sex ratio of the (titanic)")
plt.show()

#Skewness and kurtosis distribution
from scipy.stats import skew,kurtosis
ages=titanic['age'].dropna()
print("Skewness:",skew(ages))
print("kurtosis:",kurtosis(ages))

#other Distribution example uniform,binomial,poisson..
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#other distribution
uniform=np.random.uniform(0,10,1000)
binomial=np.random.binomial(0,100)
poisson=np.random.poisson(0.5,1000)
#plot
fig,ax= plt.subplots(2,2,figsize=(10,8))
sns.histplot(uniform, ax = ax[0,0], kde=False).set_title("uniform")
sns.histplot(binomial, ax = axes[1,0], kde=False).set_title("binomial")
sns.histplot(poisson, ax = axes[1,1], kde=False).set_title("poisson")
plt.tight_layout()
plt.show()
