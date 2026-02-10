import pandas as pd
study = pd.read_csv("power_nap_vs_coffee_effectiveness_dataset.csv")
print(study.columns)
study ['side_effects'] = study ['side_effects'].fillna(study = ['side_effects'].mode()[0])

print("duplicate:",study.duplicated().sum())

study.duplicated()

print(study.drop_duplicates())

print(study['occupation'].head()) #single column
print(study['occupation','age'].head())

print(study.iloc[3])

print(study.loc[0:6])

student_study = study[(study['age']>30) & (study['occupation'] == 'freelancer')]

student_study = study[(study['age']>20) | (study['occupation'] == 'student')]

print(study)
