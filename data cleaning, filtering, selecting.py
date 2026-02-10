#import libraries
import pandas as pd
#read csv file
study = pd.read_csv("power_nap_vs_coffee_effectiveness_dataset.csv")
print(study.columns)
#categories of list in  mode
study ['side_effects'] = study ['side_effects'].fillna(study = ['side_effects'].mode()[0])
#duplicate
print("duplicate:",study.duplicated().sum())
#Duplicated  
study.duplicated()
# drop duplicates
print(study.drop_duplicates())
#single column access
print(study['occupation'].head())
#multi columns accesses
print(study['occupation','age'].head())
#find the row using iloc and integer index
print(study.iloc[3])
#find the column using loc and label index
print(study.loc[0:6])
# Combining condition operation using AND operator
student_study = study[(study['age']>30) & (study['occupation'] == 'freelancer')]
# Combining condition operation using OR operator
student_study = study[(study['age']>20) | (study['occupation'] == 'student')]

